from gendiff.formatters import plain, stylish, json_format

FORMATTERS = {
    'plain': plain.make_plain,
    'json': json_format.make_json,
    'stylish': stylish.make_stylish,
}


def formator(tree, formats):
    if not tree:
        return 'Not accepted file type!'

    try:
        return FORMATTERS[formats](tree)
    except KeyError:
        return 'Wrong formatter!'
