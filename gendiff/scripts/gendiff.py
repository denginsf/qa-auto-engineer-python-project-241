from gendiff import generate_diff
import argparse
import json


def get_args():
    parser = argparse.ArgumentParser(prog='gendiff', description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args.first_file, args.second_file


def parse_json(file_path1, file_path2):
    parsed_file1 = json.load(open(f'gendiff/{file_path1}'))
    parsed_file2 = json.load(open(f'gendiff/{file_path2}'))

    return parsed_file1, parsed_file2


def main():
    first_file, second_file = get_args()
    parsed_file1, parsed_file2 = parse_json(first_file, second_file)
    generate_diff(parsed_file1, parsed_file2)

if __name__ == "__main__":
    main()