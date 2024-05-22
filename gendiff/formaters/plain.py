def to_str(value):
    if isinstance(value, list | dict):
        return '[complex value]'
    if value in ('true', 'false', 'null'):
        return value
    if value.isnumeric():
        return int(value)
    return f"'{value}'"


def make_flat(ast, start_line='Property'):  # noqa
    def walk(cur_val, parents):
        lines = []
        for data in cur_val:
            key, val = data['key'], data['value']
            cur_parents = f'{parents}.{key}' if parents else f'{key}'

            checked_val = to_str(val)
            if data['type'] == 'added':
                lines.append(f"{start_line} '{cur_parents}'"
                             f" was added with value: {checked_val}")
            elif data['type'] == 'delete':
                lines.append(f"{start_line} '{cur_parents}' was removed")
            elif data['type'] == 'unchanged' or data['type'] == 'nested':
                if not isinstance(val, dict | list):
                    continue
                lines.append(walk(val, cur_parents))
            else:
                sub_value = to_str(data['sub_value'])
                lines.append(f"{start_line} '{cur_parents}' was updated."
                             f" From {sub_value} to {checked_val}")
        return '\n'.join(lines)

    return walk(ast, '')
