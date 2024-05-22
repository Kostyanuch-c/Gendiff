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
        file_format = path_file.split('.')[-1]
        if file_format in suitable_formats:
            if file_format == 'json':
                data = json.load(file)
            else:
                data = yaml.safe_load(file)

        else:
            data = False

        return data


def pars_file(path_file):
    data = open_file(path_file)
    if isinstance(data, dict):
        get_json_and_yml_value(data)
    return data
