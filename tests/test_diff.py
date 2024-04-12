import pytest
import gendiff

tpl_input = ('tests/fixtures/first_test_diff1.json tests/fixtures/second_test_diff1.json',
             'tests/fixtures/first_test_diff1.yml tests/fixtures/second_test_diff1.yml',
             'tests/fixtures/first_test_diff2.json tests/fixtures/second_test_diff2.json',
             'tests/fixtures/first_test_diff2.yml tests/fixtures/second_test_diff2.yml')

tpl_expected = ('tests/fixtures/diff_result1.txt',
                'tests/fixtures/diff_result1.txt',
                'tests/fixtures/diff_result2.txt',
                'tests/fixtures/diff_result2.txt')


@pytest.mark.parametrize("data", zip(tpl_input, tpl_expected))
def test_json_generated_diff(data):
    test_input, expected = data
    test_file1, test_file2 = test_input.split()
    result = gendiff.generate_diff(test_file1, test_file2, 'stylish')
    with open(expected, 'r') as file:
        assert result == file.read()
