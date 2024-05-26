from gendiff.parse_files import parse_file, open_file
from gendiff.formatters import choice_formatter
from gendiff.tree_compilation import build_tree


def generate_diff(first_file, second_file, formatters='stylish'):
    formatters = choice_formatter.get_formatter(formatters)
    data1, file_format1 = open_file(first_file)
    data2, file_format2 = open_file(second_file)
    dict1 = parse_file(data1)
    dict2 = parse_file(data2)
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        tree = build_tree(dict1, dict2)
    else:
        return 'Not accepted file type!'

    return 'Wrong formatter!' if type(formatters) is str else formatters(tree)
