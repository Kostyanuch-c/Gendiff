def check_type(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value in ('true', 'false', 'null'):
        return value
    return f"'{value}'"


def make_flat(ast, start_line='Property'):  # noqa
    def walk(cur_val, parents):
        lines = []
        for key in sorted(cur_val.keys()):
            cur_parents = f'{parents}.{key}' if parents else f'{key}'
            val = cur_val[key]
            checked_val = check_type(val['value'])
            if val['type'] == 'unchanged':
                continue
            elif val['type'] == 'added':
                lines.append(f"{start_line} '{cur_parents}'"
                             f" was added with value: {checked_val}")
            elif val['type'] == 'delete':
                lines.append(f"{start_line} '{cur_parents}' was removed")
            elif (val['type'] == 'changed'
                  and not isinstance(val['value'], dict)):

                sub_value = check_type(val['sub_value'])
                lines.append(f"{start_line} '{cur_parents}' was updated."
                             f" From {sub_value} to {checked_val}")
            else:
                lines.append(walk(val['value'], cur_parents))
        return '\n'.join(lines)

    return walk(ast, '')
