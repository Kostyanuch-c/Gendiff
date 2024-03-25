#!/usr/bin/env python3.10
import argparse


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str, help='Input first file')
    parser.add_argument('second_file', type=str, help='Input second file')
    parser.add_argument(
        '-f', '--format',
        type=str,
        default='json',
        help='set format of output'
    )
    args = parser.parse_args()


if __name__ == '__main__':
    main()
