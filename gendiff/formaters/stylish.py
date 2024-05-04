from itertools import chain


def make_volume(ast_dct, replacer=' ', spaces_cnt=4, lft_shift=2):
    def walk(current_value, depth, flag=None):
        if not isinstance(current_value, dict):
            return current_value

        deep_indent_size = depth + spaces_cnt
        deep_indent = replacer * (deep_indent_size - lft_shift)
        current_indent = replacer * depth
        default = object
        lines = []
        for key in current_value.keys():
            data = current_value[key]
            if flag:
                if isinstance(data, dict):
                    if flag == '-' and data.get('sub_value', default) != default:
                        val = data["sub_value"]
                    elif data.get('value', default) != default:
                        val = data['value']
                    else:
                        val = data
                else:
                    val = data
                lines.append(f'{deep_indent}  {key}: '
                             f'{walk(val, deep_indent_size, flag)}')

            elif data['type'] == 'added' or data['type'] == 'delete':
                new_flag = '+' if data['type'] == 'added' else '-'
                lines.append(f'{deep_indent}{data["symbol"]} {key}: '
                             f'{walk(data["value"], deep_indent_size, flag=new_flag)}')
            elif data['type'] == 'unchanged':
                lines.append(f'{deep_indent}{data["symbol"]} {key}: '
                             f'{walk(data["value"], deep_indent_size)}')

            else:
                lines.append(f'{deep_indent}- {key}: {walk(data["sub_value"], deep_indent_size, flag="-")}')
                lines.append(f'{deep_indent}+ {key}: {walk(data["value"], deep_indent_size, flag="+")}')

        result = chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return walk(ast_dct, 0)
