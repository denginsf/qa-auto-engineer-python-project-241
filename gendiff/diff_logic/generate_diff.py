from gendiff.diff_logic.diff_return import diff_return
from gendiff.diff_logic.parser import parse_files
from gendiff.diff_logic.stylish import stylish


def generate_diff(file1, file2, formatter='stylish'):
    parsed_file1, parsed_file2 = parse_files(file1, file2)
    diff = diff_return(parsed_file1, parsed_file2)
    if formatter == 'stylish':
        return stylish(diff)