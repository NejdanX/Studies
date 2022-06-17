import argparse


parse = argparse.ArgumentParser()
parse.add_argument('--upper', action='store_true')
parse.add_argument('--lines', type=int, default=0)
parse.add_argument('files', nargs=2, type=str)
args = parse.parse_args()
with open(args.files[0], 'r', encoding='utf-8') as file_1:
    lines = file_1.read()
    length_file = len(lines.split('\n'))
    if args.upper:
        lines = lines.upper()
    if args.lines == 0:
        lines = lines.split('\n')
    else:
        lines = lines.split('\n')[:args.lines]
    with open(args.files[1], 'w', encoding='utf-8') as file_2:
        file_2.write('\n'.join(lines))
        if args.lines and args.lines < length_file:
            file_2.write('\n')
