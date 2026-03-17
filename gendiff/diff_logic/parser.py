import json

import yaml


def parse_file(file_name):
    with open(file_name) as f:
        if file_name.lower().endswith('.json'):
            parsed_file = json.load(f)
        elif file_name.lower().endswith(('.yml', '.yaml')):
            parsed_file = yaml.safe_load(f)
    return parsed_file


def parse_files(file_name1, file_name2):
    parsed_file1 = parse_file(file_name1)
    parsed_file2 = parse_file(file_name2)
    return parsed_file1, parsed_file2




