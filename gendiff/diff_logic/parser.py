import json

import yaml


def parse_files(file_name1, file_name2):
    with (
        open(f'gendiff/{file_name1}') as f1, 
        open(f'gendiff/{file_name2}') as f2
        ):
        if file_name1.lower().endswith('.json') \
        and file_name2.lower().endswith('.json'):
            parsed_file1 = json.load(f1)
            parsed_file2 = json.load(f2)
        elif file_name1.lower().endswith(('.yml', '.yaml')) \
        and file_name2.lower().endswith(('.yml', '.yaml')):
            parsed_file1 = yaml.safe_load(f1)
            parsed_file2 = yaml.safe_load(f2)
    return parsed_file1, parsed_file2




