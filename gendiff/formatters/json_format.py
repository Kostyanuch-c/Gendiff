import json


def make_json(ast):
    return json.dumps(ast, indent=4)
