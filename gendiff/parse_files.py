import json
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
    with open(path_file, 'r') as file:
        suitable_formats = ('json', 'yaml', 'yml')
        if path_file.endswith(suitable_formats):
            if path_file.endswith('json'):
                file_format = 'json'
            else:
                file_format = 'yaml | yml'
        else:
            file_format = ''

        return file.read(), file_format


def parse_file(data, file_format):
    if file_format == 'json':
        dct = json.loads(data)
    elif file_format == 'yaml | yml':
        dct = yaml.safe_load(data)
    else:
        return file_format

    get_json_and_yml_value(dct)
    return dct
