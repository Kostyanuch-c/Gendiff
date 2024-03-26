import json


def generate_diff(first_file, second_file):
    with (
        open(first_file, 'r') as file_1,
        open(second_file, 'r') as file_2,
    ):
        first_data, second_data = json.load(file_1), json.load(file_2)
        print(first_data)
        print(second_data)
        return None
