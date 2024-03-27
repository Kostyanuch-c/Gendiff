from itertools import chain
import json


def change_value_to_json(value):
    if value in (True, False):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def make_string(char, key, sub_value, char2=None, sub_value2=None):
    if char2:
        return (f"  {char} {key}: {sub_value}\n"
                f"  {char2} {key}: {sub_value2}")
    return f"  {char} {key}: {sub_value}"


def make_diff(key, value):
    if not value['first']:
        return make_string('+', key, value['second'])
    if not value['second']:
        return make_string('-', key, value['first'])
    if value['first'] == value['second']:
        return make_string(' ', key, value['first'])

    return make_string('-', key, value['first'], '+', value['second'])


def generate_diff(first_file, second_file):
    with (
        open(first_file, 'r') as file_1,
        open(second_file, 'r') as file_2,
    ):
        data1, data2 = json.load(file_1), json.load(file_2)
        sorted_keys = sorted(chain(data1, data2))

        combine_dct = {key: {'first': change_value_to_json(data1.get(key, '')),
                             'second': change_value_to_json(data2.get(key, ''))}
                       for key in sorted_keys}

        diff_lst = [make_diff(key, value) for key, value in combine_dct.items()]
        return '\n'.join(chain('{', diff_lst, '}'))
