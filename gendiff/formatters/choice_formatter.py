from gendiff.formatters import plain, stylish, json_format


def get_formatter(formats):
    if formats == 'plain':
        formats = plain.make_flat
    elif formats == 'json':
        formats = json_format.make_json
    elif formats == 'stylish':
        formats = stylish.make_volume

    return formats
