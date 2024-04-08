import pytest
import gendiff.pars_files
git 

@pytest.mark.parametrize("test_input,expected", [(None, 'null'), (True, 'true'), (123, '123')])
def test_get_json_value(test_input, expected):
    result = gendiff.pars_files.get_json_and_yml_value(test_input)
    assert result == expected
