from gendiff.pars_files import pars_file
from gendiff.formaters import choice_format
from gendiff.ast import build_ast


def generate_diff(first_file, second_file, formats):
    formats = choice_format.get_format(formats)
    data = list(map(pars_file, (first_file, second_file)))

    if all(data):
        ast_dct = build_ast(data[0], data[1])
    else:
        return 'Not accepted file type!'

    return formats(ast_dct) if type(formats) is not str else formats
