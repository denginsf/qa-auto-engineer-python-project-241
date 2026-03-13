from gendiff import stylish
from pathlib import Path
import json


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()

def read_json_as_dict(filename):
    file_path = get_test_data_path(filename)
    return json.loads(file_path.read_text())

def test_full_diff():
    file1 = read_json_as_dict('plain_json_first.json')
    file2 = read_json_as_dict('plain_json_second.json')
    expected = read_file("plain_json_gendiff_result.txt")
    actual = generate_diff(file1, file2)
    assert actual == expected

def test_empty_second_file():
    file1 = read_json_as_dict('plain_json_first.json')
    file2 = read_json_as_dict('empty_json.json')
    expected = read_file("empty_second_expected.txt")
    actual = generate_diff(file1, file2)
    assert actual == expected

def test_empty_first_file():
    file1 = read_json_as_dict('empty_json.json')
    file2 = read_json_as_dict('plain_json_second.json')
    expected = read_file("empty_first_expected.txt")
    actual = generate_diff(file1, file2)
    assert actual == expected

def test_empty_files():
    file1 = read_json_as_dict('empty_json.json')
    file2 = read_json_as_dict('empty_json.json')
    expected = read_file("empty_files_expected.txt")
    actual = generate_diff(file1, file2)
    assert actual == expected