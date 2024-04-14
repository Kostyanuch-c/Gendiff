import pytest
import gendiff

FORMATS = ('stylish', 'plain', 'json')
PATH_FILES = ('tests/fixtures/volume_result.txt', 'tests/fixtures/flat_result.txt', 'tests/fixtures/json_result.txt')


@pytest.fixture()
def input_json():
    return 'tests/fixtures/first_test_diff.json tests/fixtures/second_test_diff.json'


@pytest.fixture()
def input_yaml():
    return 'tests/fixtures/first_test_diff.yml tests/fixtures/second_test_diff.yml'


@pytest.fixture()
def input_yaml_and_json():
    return 'tests/fixtures/first_test_diff.yml tests/fixtures/second_test_diff.json'


@pytest.mark.parametrize("formats", ('', '1', 'G'))
def test_with_wrong_formatters(input_json, formats):
    test_path1, test_path2 = input_json.split()
    result = gendiff.generate_diff(test_path1, test_path2, formats)
    assert result == 'Wrong formatter!'


@pytest.mark.parametrize("formats", FORMATS)
def test_with_wrong_type_files(formats):
    result = gendiff.generate_diff(PATH_FILES[0], PATH_FILES[1], formats)
    assert result == 'Not accepted file type!'


@pytest.mark.parametrize("formats, path", zip(FORMATS, PATH_FILES))
def test_normal_json_file_diff(input_json, formats, path):
    test_path1, test_path2 = input_json.split()
    result = gendiff.generate_diff(test_path1, test_path2, formats)
    with open(path, 'r') as file:
        assert result == file.read()


@pytest.mark.parametrize("formats, path", zip(FORMATS, PATH_FILES))
def test_normal_yaml_file_diff(input_yaml, formats, path):
    test_path1, test_path2 = input_yaml.split()
    result = gendiff.generate_diff(test_path1, test_path2, formats)
    with open(path, 'r') as file:
        assert result == file.read()


@pytest.mark.parametrize("formats, path", zip(FORMATS, PATH_FILES))
def test_normal_yaml_file_diff(input_yaml_and_json, formats, path):
    test_path1, test_path2 = input_yaml_and_json.split()
    result = gendiff.generate_diff(test_path1, test_path2, formats)
    with open(path, 'r') as file:
        assert result == file.read()
