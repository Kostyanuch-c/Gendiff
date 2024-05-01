from itertools import chain


def make_volume(ast_dct, replacer=' ', spaces_cnt=4, lft_shift=2):  # noqa
    root_keys = sorted(root for root, value in ast_dct.items()
                       if value['value'][0] is None)

    def walk(cur_parent, depth, flag=None):
        if not isinstance(cur_parent, list) and cur_parent not in ast_dct:
            return cur_parent
        deep_indent_size = depth + spaces_cnt
        deep_indent = replacer * (deep_indent_size - lft_shift)
        current_indent = replacer * depth
        lines = []
        default = object
        for key in sorted(cur_parent):
            data = ast_dct[key]
            if flag:
                val = data["sub_value"][1] \
                    if (flag == '-'
                        and data.get('sub_value', default) != default) \
                    else data["value"][1]
                lines.append(f'{deep_indent}  {key}: '
                             f'{walk(val, deep_indent_size, flag)}')

            elif data['type'] == 'added' or data['type'] == 'delete':
                new_flg = '+' if data['type'] == 'added' else '-'
                lines.append(
                    f'{deep_indent}{data["symbol"]} {key}: '
                    f'{walk(data["value"][1], deep_indent_size, flag=new_flg)}')
            elif data['type'] == 'unchanged':
                lines.append(f'{deep_indent}{data["symbol"]} {key}: '
                             f'{walk(data["value"][1], deep_indent_size)}')
            else:
                lines.append(f'{deep_indent}- {key}: '
                             f'{walk(data["sub_value"][1], deep_indent_size)}')
                lines.append(f'{deep_indent}+ {key}: '
                             f'{walk(data["value"][1], deep_indent_size)}')

        sub_result = chain("{", lines, [current_indent + "}"])
        return '\n'.join(sub_result)

    return walk(root_keys, 0)
