#!/usr/bin/env python3.10
from gendiff import cli, generate_diff


def main():
    args = cli.parser_args()
    diff = generate_diff(args.first_file, args.second_file, formatters=args.format)
    print(diff)


if __name__ == '__main__':
    main()
