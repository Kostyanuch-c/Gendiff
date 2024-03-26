from gendiff.gendiff import generate_diff
import json
import pytest


@pytest.fixture
def coll():
    first_file_path = 'tests/fixtures/first_test_file.json'
    second_file_path = 'tests/fixtures/second_test_file.json'
    return first_file_path, second_file_path


def test_generated_diff(coll):
    result = generate_diff(coll[0], coll[1])
    assert result == ("{\n"
                      "  - follow: false\n"
                      "    host: hexlet.io\n"
                      "  - proxy: 123.234.53.22\n"
                      "  - timeout: 50\n"
                      "  + timeout: 20\n"
                      "  + verbose: true\n"
                      "}")
