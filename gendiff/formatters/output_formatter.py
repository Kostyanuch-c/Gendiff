from gendiff.formatters import plain, stylish, json_format


def get_diff(tree, formats):
    if not tree:
        return 'Not accepted file type!'

    if formats == 'plain':
        return plain.make_flat(tree)
    elif formats == 'json':
        return json_format.make_json(tree)
    elif formats == 'stylish':
        return stylish.make_volume(tree)

    else:
        return 'Wrong formatter!'
