from os import listdir, stat
from os.path import isfile


def human_read_format(size):
    names = ['Б', 'КБ', 'МБ', 'ГБ']
    count_operation = 0
    while size > 1023:
        count_operation += 1
        size /= 1024
    return f'{round(size)}{names[count_operation]}'


def get_files_sizes():
    files = [f for f in listdir() if isfile(f)]
    return '\n'.join([f'{file} {human_read_format(stat(file).st_size)}' for file in files])


print(get_files_sizes())
