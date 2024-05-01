import copy
from gendiff.pars_files import pars_file
from gendiff.formaters import plain, stylish, json_format


def make_joints(tree, dictionary, parent=None):
    if not isinstance(tree, dict):
        return tree
    children = []

    for key in tree.keys():
        name = make_joints(tree[key], dictionary, parent=key)
        children.append(name)
        new_children = copy.deepcopy(children)
        children.clear()
        dictionary[key] = (parent, *new_children)

    return list(tree.keys())


def build_ast(cur_dct1, cur_dct2, result={}):
    keys = cur_dct2.keys() | cur_dct1.keys()
    for key in sorted(keys):
        if key not in cur_dct1:
            result[key] = {'value': cur_dct2[key],
                           'type': 'added',
                           'symbol': '+'}
        elif key not in cur_dct2:
            result[key] = {'value': cur_dct1[key],
                           'type': 'delete',
                           'symbol': '-'}

        elif (cur_dct1[key][1] == cur_dct2[key][1]
              or isinstance(cur_dct1[key][1], list)
              and isinstance(cur_dct2[key][1], list)
              and any(True if x in cur_dct1[key][1]
                      else False for x in cur_dct2[key][1])):

            if (isinstance(cur_dct1[key][1], list)
                    and isinstance(cur_dct2[key][1], list)):
                child = set(cur_dct2[key][1]) | set(cur_dct1[key][1])
                val = (cur_dct2[key][0], sorted(list(child)))
            else:
                val = cur_dct2[key]

            result[key] = {'value': val,
                           'type': 'unchanged',
                           'symbol': ' '}
        else:
            result[key] = {'value': cur_dct2[key],
                           'sub_value': cur_dct1[key],
                           'type': 'changed',
                           'symbol': ' '}
    return result


def generate_diff(first_file, second_file, formats=stylish.make_volume):
    if isinstance(formats, str):
        if formats == 'plain':
            formats = plain.make_flat
        elif formats == 'json':
            formats = json_format.make_json
        elif formats == 'stylish':
            formats = stylish.make_volume
        else:
            return 'Wrong formatter!'
    data1, data2 = pars_file(first_file, second_file)
    if not data1:
        return 'Not accepted file type!'

    d1 = {}
    d2 = {}
    make_joints(data1, d1)
    make_joints(data2, d2)

    ast_dct = build_ast(d1, d2)
    return formats(ast_dct)
