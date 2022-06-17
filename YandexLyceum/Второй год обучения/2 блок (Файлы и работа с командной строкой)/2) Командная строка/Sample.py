import sys


print(sys.argv)
is_sort = '--sort' in sys.argv
args = sys.argv[1:]
args.remove('--sort') if is_sort else 0
result = [{'Key': item.split("=")[0], 'Value': item.split("=")[1]}for item in args]
if is_sort:
    result = sorted(result, key=lambda x: x['Key'])
for item in result:
    for key, value in item.items():
        print(f'{key}: {value}', end=' ')
    print()