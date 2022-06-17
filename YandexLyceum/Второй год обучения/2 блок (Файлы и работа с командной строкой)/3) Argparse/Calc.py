import argparse


parser = argparse.ArgumentParser()
parser.add_argument('numbers', nargs='*')
args = parser.parse_args()
if not args.numbers:
    print('NO PARAMS')
elif len(args.numbers) == 1:
    print('TOO FEW PARAMS')
elif len(args.numbers) > 2:
    print('TOO MANY PARAMS')
else:
    try:
        print(sum(map(int, args.numbers)))
    except TypeError as e:
        print(e.__class__.__name__)
    except ValueError as e:
        print(e.__class__.__name__)
    except Exception as e:
        print(e.__class__.__name__)