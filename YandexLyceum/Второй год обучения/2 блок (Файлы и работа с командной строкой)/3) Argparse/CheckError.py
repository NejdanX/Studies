import argparse


def print_error(message):
    print(f'ERROR: {message}!!')


if __name__ == '__main__':
    print('Welcome to my program')
    parser = argparse.ArgumentParser()
    parser.add_argument('string', nargs='+')
    arg = parser.parse_args()
    print_error(' '.join(arg.string))