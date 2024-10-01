import json
import os

import yaml


def get_json_and_yml_value(current_value):
    if current_value in (True, False):
        return str(current_value).lower()
    if current_value is None:
        return 'null'
    if not isinstance(current_value, dict):
        return str(current_value)
    for k, v in current_value.items():
        new_value = get_json_and_yml_value(v)
        new_item = {k: new_value}
        if new_value:
            current_value.update(new_item)


def open_file(path_file):
    extension = os.path.splitext(path_file)[-1]

    with open(path_file, 'r', encoding='utf-8') as file:
        data = file.read()

    if extension == '.json':
        file_format = 'json'
    elif extension in ('.yaml', '.yml'):
        file_format = 'yaml'
    else:
        file_format = ''

    return data, file_format


def parse_file(data, file_format):
    if file_format == 'json':
        dictionary = json.loads(data)
    elif file_format == 'yaml':
        dictionary = yaml.safe_load(data)
    else:
        return file_format

    get_json_and_yml_value(dictionary)
    return dictionary


def open_and_parse_file(path_file):
    data, file_format = open_file(path_file)
    return parse_file(data, file_format)
