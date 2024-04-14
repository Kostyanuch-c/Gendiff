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


def pars_file(path_first_file, path_second_file):
    with (
        open(path_first_file, 'r') as file_1,
        open(path_second_file, 'r') as file_2,
    ):
        suitable_format = ('json', 'yaml', 'yml')
        first_file_format = path_first_file.split('.')[-1]
        second_file_format = path_second_file.split('.')[-1]
        if (first_file_format in suitable_format
                and second_file_format in suitable_format):
            if first_file_format == 'json':
                data1 = json.load(file_1)
            else:
                data1 = yaml.safe_load(file_1)
            if second_file_format == 'json':
                data2 = json.load(file_2)
            else:
                data2 = yaml.safe_load(file_2)

            list(map(get_json_and_yml_value, (data1, data2)))
        else:
            data1, data2 = '', ''
        return data1, data2
