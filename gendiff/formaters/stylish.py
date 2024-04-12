from itertools import chain


def make_volume(ast_dct, replacer=' ', spaces_cnt=4, lft_shift=2):  # noqa
    def walk(current_value, depth):
        if not isinstance(current_value, dict):
            return current_value

        deep_indent_size = depth + spaces_cnt
        deep_indent = replacer * (deep_indent_size - lft_shift)
        current_indent = replacer * depth
        default = object
        lines = []
        for key in sorted(current_value.keys()):
            val = current_value[key]
            if not isinstance(val, dict):
                lines.append(f'{deep_indent}  {key}: {val}')

            elif val.get('type', default) == default:
                lines.append(f'{deep_indent}  {key}: '
                             f'{walk(val, deep_indent_size)}')
            elif val['type'] == 'changed' and not isinstance(val['value'],
                                                             dict):
                sub_value = val['sub_value']
                if isinstance(sub_value, dict):
                    sub_value = walk(sub_value, deep_indent_size)

                lines.append(f'{deep_indent}- {key}: {sub_value}')
                lines.append(f'{deep_indent}+ {key}: {val["value"]}')

            else:
                lines.append(f'{deep_indent}{val["symbol"]} {key}: '
                             f'{walk(val["value"], deep_indent_size)}')

        result = chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return walk(ast_dct, 0)
