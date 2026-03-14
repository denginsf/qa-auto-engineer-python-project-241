from gendiff import generate_diff
from pathlib import Path
import json


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename

def read_file(filename):
    return get_test_data_path(filename).read_text()

# JSON тесты

def test_full_diff():
    file1 = str(get_test_data_path('plain_json_first.json'))
    file2 = str(get_test_data_path('plain_json_second.json'))
    expected = read_file("plain_json_and_yaml_gendiff_result.txt")
    actual = generate_diff(file1, file2)
    assert expected == actual

def test_empty_first_file():
    file1 = str(get_test_data_path('empty_json.json'))
    file2 = str(get_test_data_path('plain_json_second.json'))
    expected = read_file("empty_first_expected.txt")
    actual = generate_diff(file1, file2)
    assert actual == expected

def test_empty_second_file():
    file1 = str(get_test_data_path('plain_json_first.json'))
    file2 = str(get_test_data_path('empty_json.json'))
    expected = read_file("empty_second_expected.txt")
    actual = generate_diff(file1, file2)
    assert expected == actual

def test_empty_files():
    file1 = str(get_test_data_path('empty_json.json'))
    file2 = str(get_test_data_path('empty_json.json'))
    expected = read_file("empty_files_expected.txt")
    actual = generate_diff(file1, file2)
    assert actual == expected

# YAML тесты
# Еще проверяею расгирение .yml .yaml

def test_full_diff_yaml():
    file1 = str(get_test_data_path('test_file1.yml'))
    file2 = str(get_test_data_path('test_file2.yaml'))
    expected = read_file("plain_json_and_yaml_gendiff_result.txt")
    actual = generate_diff(file1, file2)
    assert actual == expected

def test_empty_first_file_yaml():
    file1 = str(get_test_data_path('empty_yaml.yml'))
    file2 = str(get_test_data_path('test_file2.yaml'))
    expected = read_file("empty_first_expected.txt")
    actual = generate_diff(file1, file2)
    assert actual == expected

def test_empty_second_file_yaml():
    file1 = str(get_test_data_path('test_file1.yml'))
    file2 = str(get_test_data_path('empty_yaml.yml'))
    expected = read_file("empty_second_expected.txt")
    actual = generate_diff(file1, file2)
    assert actual == expected

def test_empty_files_yaml():
    file1 = str(get_test_data_path('empty_yaml.yml'))
    file2 = str(get_test_data_path('empty_yaml.yml'))
    expected = read_file("empty_files_expected.txt")
    actual = generate_diff(file1, file2)
    assert actual == expected