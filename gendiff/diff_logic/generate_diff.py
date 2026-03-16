from gendiff.diff_logic.diff_return import diff_return
from gendiff.diff_logic.parser import parse_files
from gendiff.formatters.plain_formatter import plain
from gendiff.formatters.stylish_formatter import stylish


def generate_diff(file1, file2, format='stylish'):
    parsed_file1, parsed_file2 = parse_files(file1, file2)
    diff = diff_return(parsed_file1, parsed_file2)
    if format == 'stylish':
        return stylish(diff)
    if format == 'plain':
        return plain(diff)