import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--count', action='store_true')
parser.add_argument('--num', action='store_true')
parser.add_argument('--sort', action='store_true')
parser.add_argument('file', nargs=1, type=str)
args = parser.parse_args()
try:
    with open(args.file[0], 'r', encoding='utf-8') as file:
        lines = list(map(str.strip, file.readlines()))
        if args.sort:
            lines.sort()
        for i in range(len(lines)):
            print(f'{i} {lines[i]}' if args.num else lines[i])
        if args.count:
            print('rows count:', len(lines))
except Exception as e:
    print('ERROR' if e.__class__.__name__ else 'ERROR')

