import copy
from gendiff.pars_files import pars_file
from gendiff.formaters import plain, stylish, json_format


def build_ast(current_dct1, current_dct2, result={}, acc={}):
    keys = current_dct1.keys() | current_dct2.keys()
    acc = copy.deepcopy(result)
    result.clear()
    for key in sorted(keys):
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
                           'type': 'unchanged',
                           'symbol': ' '}
        else:
            value = build_ast(current_dct1[key], current_dct2[key],
                              acc, result) \
                if isinstance(current_dct2[key], dict) \
                else current_dct2[key]

            result[key] = {'value': value,
                           'sub_value': current_dct1[key],
                           'type': 'changed',
                           'symbol': ' '}

    new_value = copy.deepcopy(result)
    return new_value


# def generate_diff(first_file, second_file, formats=stylish.make_volume):
#     if isinstance(formats, str):
#         if formats == 'plain':
#             formats = plain.make_flat
#         elif formats == 'json':
#             formats = json_format.make_json
#         elif formats == 'stylish':
#             formats = stylish.make_volume
#         else:
#             return 'Wrong formatter!'
#     data1, data2 = pars_file(first_file, second_file)
#     if not data1:
#         return 'Not accepted file type!'
#     ast_dct = build_ast(data1, data2)
#     return formats(ast_dct)
def generate_diff(first_file, second_file, formats):
    if formats == 'stylish':
        formats = stylish.make_volume
    else:
        formats = plain.make_flat
    data1, data2 = pars_file(first_file, second_file)
    ast_dct = build_ast(data1, data2)
    return formats(ast_dct)