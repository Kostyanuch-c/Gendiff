from gendiff.formatters import plain, stylish, json_format


def formator(tree, formats):
    if not tree:
        return 'Not accepted file type!'

    if formats == 'plain':
        return plain.make_plain(tree)
    elif formats == 'json':
        return json_format.make_json(tree)
    elif formats == 'stylish':
        return stylish.make_stylish(tree)
    else:
        return 'Wrong formatter!'
