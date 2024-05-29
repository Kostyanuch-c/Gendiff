def build_tree(data1, data2):  # noqa
    if not isinstance(data1, dict) or not isinstance(data2, dict):
        return None

    def walk(current_dct1, current_dct2):
        if isinstance(current_dct2, str):
            return current_dct2
        keys = current_dct2.keys() if isinstance(current_dct1, str) \
            else current_dct1.keys() | current_dct2.keys()
        result = []
        for key in sorted(keys):

            if key not in current_dct1:
                result.append({'value': current_dct2[key],
                               'type': 'added',
                               'key': f'{key}',
                               'symbol': '+'})
            elif key not in current_dct2:
                result.append({'value': current_dct1[key],
                               'type': 'delete',
                               'key': f'{key}',
                               'symbol': '-'})
            elif (isinstance(current_dct1[key], dict)
                  and isinstance(current_dct2[key], dict)):
                result.append({'value': walk(current_dct1[key],
                                             current_dct2[key],
                                             ),
                               'type': 'nested',
                               'key': f'{key}',
                               'symbol': ' '})
            elif current_dct1[key] == current_dct2[key]:
                result.append({'value': walk(current_dct1[key],
                                             current_dct2[key],
                                             ),
                               'type': 'unchanged',
                               'key': f'{key}',
                               'symbol': ' '})
            else:
                result.append({'value': walk(current_dct1[key],
                                             current_dct2[key],
                                             ),
                               'sub_value': current_dct1[key],
                               'type': 'changed',
                               'key': f'{key}',
                               'symbol': ' '})

        return result

    return walk(data1, data2)
