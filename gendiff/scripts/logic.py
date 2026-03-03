import argparse
import json
    
def get_args():
    parser = argparse.ArgumentParser(prog='gendiff', description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    parsed_file1 = json.load(open(f'qa-auto-engineer-python-project-241/gendiff/{args.first_file}'))
    parsed_file2 = json.load(open(f'qa-auto-engineer-python-project-241/gendiff/{args.second_file}'))
    print(parsed_file1)
    return parsed_file1, parsed_file2