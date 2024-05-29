from itertools import chain

SPACES_COUNTER = 4
LEFT_SHIFT = 2


def make_stylish(tree, replacer=' '):
    def walk(current_value, depth, flag=None):
        if not isinstance(current_value, dict | list):
            return current_value

        deep_indent_size = depth + SPACES_COUNTER
        deep_indent = replacer * (deep_indent_size - LEFT_SHIFT)
        current_indent = replacer * depth
        default = object
        lines = []
        for data in current_value:
            if (isinstance(current_value, dict)
               and current_value.get('type', default) == default):
                lines.append(
                    f'{deep_indent}  {data}: '
                    f'{walk(current_value[data], deep_indent_size, flag)}')
                continue

            value = data['value']
            if data['type'] == 'changed':
                lines.append(
                    f'{deep_indent}- {data["key"]}: '
                    f'{walk(data["sub_value"], deep_indent_size, flag="-")}')
                lines.append(
                    f'{deep_indent}+ {data["key"]}: '
                    f'{walk(value, deep_indent_size, flag="+")}')

            else:
                symbol = data["symbol"] if not flag else ' '
                lines.append(
                    f'{deep_indent}{symbol} {data["key"]}: '
                    f'{walk(value, deep_indent_size)}')

        result = chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return walk(tree, 0)
