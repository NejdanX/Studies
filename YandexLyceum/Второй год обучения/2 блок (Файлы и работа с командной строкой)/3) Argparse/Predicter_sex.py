import argparse
MOVIES_SCORES = {'melodrama': 0, 'football': 100, 'other': 50}

parser = argparse.ArgumentParser()
parser.add_argument('--barbie',
                    choices=range(0, 101),
                    default=50
                    )
parser.add_argument('--cars',
                    choices=range(0, 101),
                    default=50
                    )
parser.add_argument('--movie',
                    choices=['melodrama', 'football', 'other'],
                    default='other'
                    )
args = parser.parse_args()
boy = int((100 - args.barbie + args.cars + MOVIES_SCORES[args.movie]) / 3)
girl = 100 - boy
print(f'boy: {boy}\ngirl: {girl}')