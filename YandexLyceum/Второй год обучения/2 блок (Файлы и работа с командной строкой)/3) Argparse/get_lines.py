import argparse


def count_lines(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return len(file.readlines())
    except FileNotFoundError:
        return 0
    except FileExistsError:
        return 0
    except TypeError:
        return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')
    args = parser.parse_args()
    if not args:
        print(0)
        exit(0)
    print(count_lines(args.file))

