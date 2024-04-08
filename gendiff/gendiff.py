import copy
from itertools import chain
from gendiff.pars_files import pars_file


def stringify(ast_dct, replacer=' ', spaces_cnt=4, lft_shift=2):
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
                continue
            if val.get('type', default) == default:
                lines.append(f'{deep_indent}  {key}: '
                             f'{walk(val, deep_indent_size)}')
                continue
            if val['type'] == 'changed' and not isinstance(val['value'], dict):
                sub_value = val['sub_value']
                if isinstance(sub_value, dict):
                    sub_value = walk(sub_value, deep_indent_size)

                lines.append(f'{deep_indent}- {key}: {sub_value}')
                lines.append(f'{deep_indent}+ {key}: {val["value"]}')
                continue
            if val['type'] == 'added' or val['type'] == 'delete':
                lines.append(f'{deep_indent}{val["symbol"]} {key}: '
                             f'{walk(val["value"], deep_indent_size)}')
                continue

            lines.append(f'{deep_indent}  {key}: '
                         f'{walk(val["value"], deep_indent_size)}')

        result = chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return walk(ast_dct, 0)


def build_ast(current_dct1, current_dct2, result={}, acc={}):
    keys = current_dct1.keys() | current_dct2.keys()
    acc = copy.deepcopy(result)
    result.clear()
    for key in keys:
        if key not in current_dct1:
            result[key] = {'value': current_dct2[key],
                           'type': 'added',
                           'symbol': '+'}
        elif key not in current_dct2:
            result[key] = {'value': current_dct1[key],
                           'type': 'delete',
                           'symbol': '-'}
        elif current_dct1[key] == current_dct2[key]:
            value = build_ast(current_dct1[key], current_dct2[key],
                              acc, result) \
                if isinstance(current_dct1[key], dict) \
                else current_dct1[key]

            result[key] = {'value': value,
                           'type': 'unchanged'}
        else:
            value = build_ast(current_dct1[key], current_dct2[key],
                              acc, result) \
                if isinstance(current_dct2[key], dict) \
                else current_dct2[key]

            result[key] = {'value': value,
                           'sub_value': current_dct1[key],
                           'type': 'changed'}

    new_value = copy.deepcopy(result)
    return new_value


def generate_diff(first_file, second_file, formats=stringify):
    data1, data2 = pars_file(first_file, second_file)
    ast_dct = build_ast(data1, data2)
    return formats(ast_dct)
