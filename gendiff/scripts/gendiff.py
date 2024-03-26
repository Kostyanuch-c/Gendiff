#!/usr/bin/env python3.10

# noinspection PyUnresolvedReferences
from gendiff import cli, generate_diff


def main():
    args = cli.parser_args()
    generate_diff(args.first_file, args.second_file)

    return None


if __name__ == '__main__':
    main()
