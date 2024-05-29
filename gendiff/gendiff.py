from gendiff.parse_files import open_and_parse_file
from gendiff.formatters.output_formatter import formator
from gendiff.tree_compilation import build_tree


def generate_diff(first_file, second_file, formatters='stylish'):
    dict1 = open_and_parse_file(first_file)
    dict2 = open_and_parse_file(second_file)

    tree = build_tree(dict1, dict2)
    return formator(tree, formatters)
