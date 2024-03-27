from gendiff.gendiff import generate_diff
import pytest


@pytest.fixture
def coll():
    first_file_path = 'tests/fixtures/first_test_file.json'
    second_file_path = 'tests/fixtures/second_test_file.json'
    return first_file_path, second_file_path


def test_generated_diff(coll):
    result = generate_diff(coll[0], coll[1])
    with open('tests/fixtures/guess_result.txt', 'r') as guess_result:
        assert result == guess_result.read()
