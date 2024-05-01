def check_type(value):
    if isinstance(value[1], list):
        return '[complex value]'
    if value[1] in ('true', 'false', 'null'):
        return value[1]
    return f"'{value[1]}'"


def make_flat(ast_dct, start_line='Property'): # noqa
    root_keys = sorted(root for root, value in ast_dct.items()
                       if value['value'][0] is None)

    def walk(cur_val, parents):
        lines = []
        for key in sorted(cur_val):
            cur_parents = f'{parents}.{key}' if parents else f'{key}'
            val = ast_dct[key]
            checked_val = check_type(val['value'])
            if val['type'] == 'added':
                lines.append(f"{start_line} '{cur_parents}'"
                             f" was added with value: {checked_val}")
            elif val['type'] == 'delete':
                lines.append(f"{start_line} '{cur_parents}' was removed")
            elif val['type'] == 'unchanged':
                if not isinstance(val['value'][1], list):
                    continue
                lines.append(walk(val['value'][1], cur_parents))
            else:
                sub_value = check_type(val['sub_value'])
                lines.append(f"{start_line} '{cur_parents}' was updated."
                             f" From {sub_value} to {checked_val}")

        return '\n'.join(lines)

    return walk(root_keys, '')
