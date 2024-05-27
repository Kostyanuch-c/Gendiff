from gendiff.parse_files import parse_file, open_file
from gendiff.formatters import output_formatter
from gendiff.tree_compilation import build_tree


def generate_diff(first_file, second_file, formatters='stylish'):
    data1, file_format1 = open_file(first_file)
    data2, file_format2 = open_file(second_file)

    dict1 = parse_file(data1, file_format1)
    dict2 = parse_file(data2, file_format2)

    return output_formatter.get_diff(build_tree(dict1, dict2), formatters)
