def to_str(value):
    if isinstance(value, list | dict):
        return '[complex value]'
    if value in ('true', 'false', 'null'):
        return value
    if value.isnumeric():
        return int(value)
    return f"'{value}'"


def make_plain(tree, start_line='Property'):  # noqa
    def walk(current_value, parents):
        lines = []
        for data in current_value:
            key, value = data['key'], data['value']
            current_parents = f'{parents}.{key}' if parents else f'{key}'

            prepared_value = to_str(value)
            if data['type'] == 'added':
                lines.append(f"{start_line} '{current_parents}'"
                             f" was added with value: {prepared_value}")
            elif data['type'] == 'delete':
                lines.append(f"{start_line} '{current_parents}' was removed")
            elif data['type'] == 'unchanged' or data['type'] == 'nested':
                if not isinstance(value, dict | list):
                    continue
                lines.append(walk(value, current_parents))
            else:
                sub_value = to_str(data['sub_value'])
                lines.append(f"{start_line} '{current_parents}' was updated."
                             f" From {sub_value} to {prepared_value}")
        return '\n'.join(lines)

    return walk(tree, '')
