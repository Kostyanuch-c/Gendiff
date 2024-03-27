import gendiff.gendiff
import pytest


@pytest.fixture
def coll():
    first_file_path = 'tests/fixtures/first_test_file.json'
    second_file_path = 'tests/fixtures/second_test_file.json'
    return first_file_path, second_file_path


@pytest.mark.parametrize("test_input,expected", [(None, 'null'), (True, 'true'), (123, '123')])
def test_get_json_value(test_input, expected):
    result = gendiff.gendiff.get_json_value(test_input)
    assert result == expected


def test_generated_diff(coll):
    result = gendiff.generate_diff(coll[0], coll[1])
    with open('tests/fixtures/guess_result.txt', 'r') as guess_result:
        assert result == guess_result.read()
