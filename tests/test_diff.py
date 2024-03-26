import json
from gendiff.generating_diff import generate_diff
import pytest


@pytest.fixture
def coll():
    first_file = '''{
      "host": "hexlet.io",
      "timeout": 50,
      "proxy": "123.234.53.22",
      "follow": false
    }'''

    second_file = '''{
      "timeout": 20,
      "verbose": true,
      "host": "hexlet.io"
    }'''
    data_1 = json.loads(first_file)
    data_2 = json.loads(second_file)
    with (
        open('first_test_file.json', 'w') as file_1,
        open('second_test_file.json', 'w') as file_2,
    ):
        json.dump(data_1, file_1)
        json.dump(data_2, file_2)

        return './first_test_file.json', './second_test_file.json'


def test_generated_diff(coll):
    result = generate_diff(coll[0], coll[1])
    assert result is None
