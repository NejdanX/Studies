import argparse


parser = argparse.ArgumentParser()
parser.add_argument('others', nargs='*')
parser.add_argument('--sort', action='store_true')
args = parser.parse_args()
if args.sort:
    args.others.sort(key=lambda x: x.split('=')[0])
dictionary = {arg.split('=')[0]: arg.split('=')[1] for arg in args.others}
for key, value in dictionary.items():
    print(f'Key: {key}\t\tValue: {value}')