import argparse

from gendiff import generate_diff


def get_args():
    parser = argparse.ArgumentParser(prog='gendiff', 
    description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', 
    help='set format of output (default: "stylish")', default='stylish')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format


def main():
    first_file, second_file, format_name = get_args()
    base_path = \
    '/Users/alekseidengin/qa-auto-engineer-python-project-241/tests/files_for_script_run'
    first_path = f'{base_path}/{first_file}'
    second_path = f'{base_path}/{second_file}'
    generate_diff(first_path, second_path, format_name)
    print(generate_diff(first_path, second_path, format_name))


if __name__ == "__main__":
    main()