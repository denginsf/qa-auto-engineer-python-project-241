import argparse

from gendiff import generate_diff


def get_args():
    parser = argparse.ArgumentParser(prog='gendiff', 
    description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', 
    help='set format of output', default='stylish')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format


def main():
    first_file, second_file, format_name = get_args()
    generate_diff(first_file, second_file, format_name)
    print(generate_diff(first_file, second_file, format_name))


if __name__ == "__main__":
    main()