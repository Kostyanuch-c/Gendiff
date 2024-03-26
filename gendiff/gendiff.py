import json


def update_value(value):
    if value in (True, False):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def update_string(diff1, diff2):
    if diff1 and diff2:
        if diff1[1] == diff2[1]:
            added_str = f"    {': '.join(diff1)}\n"
            return added_str
        added_str1 = f"  - {': '.join(diff1)}\n"
        added_str2 = f"  + {': '.join(diff2)}\n"
        return added_str1 + added_str2
    if diff1:
        added_str = f"  - {': '.join(diff1)}\n"
        return added_str
    if diff2:
        added_str = f"  + {': '.join(diff2)}\n"
        return added_str


def generate_diff(first_file, second_file):
    with (
        open(first_file, 'r') as file_1,
        open(second_file, 'r') as file_2,
    ):
        first_data, second_data = json.load(file_1), json.load(file_2)
        sorted_keys = sorted(set(first_data).union(set(second_data)))

        string = '{\n'
        default = object
        for key in sorted_keys:
            diff1 = []
            diff2 = []
            value1 = update_value(first_data.get(key, default))
            value2 = update_value(second_data.get(key, default))
            if key in first_data and key in second_data:
                if value1 == value2:
                    diff1.extend([key, value1])
                    diff2.extend([key, value2])
                else:
                    diff1.extend([key, value1])
                    diff2.extend([key, value2])
            elif key in first_data:
                diff1.extend([key, value1])
            else:
                diff2.extend([key, value2])

            added_string = update_string(diff1, diff2)
            string += added_string
        return string + '}'
