import argparse
import os

from gendiff import generate_diff


def get_args():
    parser = argparse.ArgumentParser(prog='gendiff', 
    description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args.first_file, args.second_file


def main():
    first_file, second_file = get_args()
    generate_diff(first_file, second_file)
    print(generate_diff(first_file, second_file))


if __name__ == "__main__":
    main()