from pathlib import Path

from gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()

# Stylish

# JSON тесты


def test_stylish_formatter_plain_json_full_diff():
    file1 = str(get_test_data_path('plain_json_first.json'))
    file2 = str(get_test_data_path('plain_json_second.json'))
    expected = read_file("plain_json_and_yaml_gendiff_result.txt")
    actual = generate_diff(file1, file2)
    assert expected == actual


def test_stylish_formatter_plain_json_empty_first_file():
    file1 = str(get_test_data_path('empty_json.json'))
    file2 = str(get_test_data_path('plain_json_second.json'))
    expected = read_file("empty_first_expected.txt")
    actual = generate_diff(file1, file2)
    assert actual == expected


def test_stylish_formatter_plain_json_empty_second_file():
    file1 = str(get_test_data_path('plain_json_first.json'))
    file2 = str(get_test_data_path('empty_json.json'))
    expected = read_file("empty_second_expected.txt")
    actual = generate_diff(file1, file2)
    assert expected == actual


def test_stylish_formatter_plain_json_empty_files():
    file1 = str(get_test_data_path('empty_json.json'))
    file2 = str(get_test_data_path('empty_json.json'))
    expected = read_file("empty_files_expected.txt")
    actual = generate_diff(file1, file2)
    assert actual == expected

# YAML тесты
# Еще проверяею расширение .yml .yaml


def test_stylish_formatter_full_diff_plain_yaml():
    file1 = str(get_test_data_path('test_file1.yml'))
    file2 = str(get_test_data_path('test_file2.yaml'))
    expected = read_file("plain_json_and_yaml_gendiff_result.txt")
    actual = generate_diff(file1, file2)
    assert actual == expected


def test_stylish_formatter_empty_first_file_plain_yaml():
    file1 = str(get_test_data_path('empty_yaml.yml'))
    file2 = str(get_test_data_path('test_file2.yaml'))
    expected = read_file("empty_first_expected.txt")
    actual = generate_diff(file1, file2)
    assert actual == expected


def test_stylish_formatter_empty_second_file_plain_yaml():
    file1 = str(get_test_data_path('test_file1.yml'))
    file2 = str(get_test_data_path('empty_yaml.yml'))
    expected = read_file("empty_second_expected.txt")
    actual = generate_diff(file1, file2)
    assert actual == expected


def test_stylish_formatter_empty_files_plain_yaml():
    file1 = str(get_test_data_path('empty_yaml.yml'))
    file2 = str(get_test_data_path('empty_yaml.yml'))
    expected = read_file("empty_files_expected.txt")
    actual = generate_diff(file1, file2)
    assert actual == expected


# Plain

# JSON тесты plain formatter

def test_plain_formatter_plain_json_full_diff():
    file1 = str(get_test_data_path('plain_json_first.json'))
    file2 = str(get_test_data_path('plain_json_second.json'))
    expected = read_file("plain_formatter_json_and_yaml_gendiff_result.txt")
    actual = generate_diff(file1, file2, 'plain')
    assert expected == actual


def test_plain_formatter_plain_json_empty_first_file():
    file1 = str(get_test_data_path('empty_json.json'))
    file2 = str(get_test_data_path('plain_json_second.json'))
    expected = read_file("plain_formatter_empty_first_expected.txt")
    actual = generate_diff(file1, file2, 'plain')
    assert actual == expected


def test_plain_formatter_plain_json_second_file():
    file1 = str(get_test_data_path('plain_json_first.json'))
    file2 = str(get_test_data_path('empty_json.json'))
    expected = read_file("plain_formatter_empty_second_expected.txt")
    actual = generate_diff(file1, file2, 'plain')
    assert expected == actual


def test_plain_formatter_plain_json_files():
    file1 = str(get_test_data_path('empty_json.json'))
    file2 = str(get_test_data_path('empty_json.json'))
    expected = read_file("plain_formatter_empty_files_expected.txt")
    actual = generate_diff(file1, file2, 'plain')
    assert actual == expected

# YAML тесты plain formatter
# Еще проверяею расширение .yml .yaml


def test_plain_formatter_full_diff_plain_yaml():
    file1 = str(get_test_data_path('test_file1.yml'))
    file2 = str(get_test_data_path('test_file2.yaml'))
    expected = read_file("plain_formatter_json_and_yaml_gendiff_result.txt")
    actual = generate_diff(file1, file2, 'plain')
    assert actual == expected


def test__plain_formatter_empty_first_plain_yaml():
    file1 = str(get_test_data_path('empty_yaml.yml'))
    file2 = str(get_test_data_path('test_file2.yaml'))
    expected = read_file("plain_formatter_empty_first_expected.txt")
    actual = generate_diff(file1, file2, 'plain')
    assert actual == expected


def test__plain_formatter_empty_second_plain_yaml():
    file1 = str(get_test_data_path('test_file1.yml'))
    file2 = str(get_test_data_path('empty_yaml.yml'))
    expected = read_file("plain_formatter_empty_second_expected.txt")
    actual = generate_diff(file1, file2, 'plain')
    assert actual == expected


def test__plain_formatter_empty_files_plain_yaml():
    file1 = str(get_test_data_path('empty_yaml.yml'))
    file2 = str(get_test_data_path('empty_yaml.yml'))
    expected = read_file("plain_formatter_empty_files_expected.txt")
    actual = generate_diff(file1, file2, 'plain')
    assert actual == expected