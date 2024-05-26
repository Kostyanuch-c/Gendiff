from itertools import chain

SPACES_CNT = 4
LFT_SHIFT = 2


def make_volume(ast_dct, replacer=' '):
    def walk(cur_value, depth, flag=None):
        if not isinstance(cur_value, dict | list):
            return cur_value

        deep_indent_size = depth + SPACES_CNT
        deep_indent = replacer * (deep_indent_size - LFT_SHIFT)
        current_indent = replacer * depth
        default = object
        lines = []
        for data in cur_value:
            if (isinstance(cur_value, dict)
                    and cur_value.get('type', default) == default):
                lines.append(f'{deep_indent}  {data}: '
                             f'{walk(cur_value[data], deep_indent_size, flag)}')
                continue

            value = data['value']
            if data['type'] == 'changed':
                lines.append(
                    f'{deep_indent}- {data["key"]}:'
                    f' {walk(data["sub_value"], deep_indent_size, flag="-")}')
                lines.append(
                    f'{deep_indent}+ {data["key"]}:'
                    f' {walk(value, deep_indent_size, flag="+")}')

            else:
                symbol = data["symbol"] if not flag else ' '
                lines.append(
                    f'{deep_indent}{symbol} {data["key"]}: '
                    f'{walk(value, deep_indent_size)}')

        result = chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return walk(ast_dct, 0)
