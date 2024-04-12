import argparse


def parser_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument(
        '-f', '--format',
        type=str,
        default='stylish',
        help='set format of output'
    )
    parser.add_argument('first_file',
                        type=str,
                        help='Input path to first file')
    parser.add_argument('second_file',
                        type=str,
                        help='Input path to second file')

    args = parser.parse_args()

    return args
