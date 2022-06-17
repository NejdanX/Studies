UNITS = {
    'B': 1,
    'KB': 1024,
    'MB': 1024 ** 2,
    'GB': 1024 ** 3,
    'TB': 1024 ** 4
}


file_information = {}
with open('input.txt', encoding='utf8') as file:
    for line in file.readlines():
        name, size, unit = line.split()
        size = int(size)
        name, extension = name.split('.')
        if extension in file_information:
            file_information[extension][0].append(name)
            file_information[extension][1] += (size * UNITS[unit])
        else:
            file_information[extension] = [[name], size * UNITS[unit]]

with open('output.txt', 'w', encoding='utf8') as file:
    keys = sorted(file_information.keys())
    for extension in keys:
        names, size = file_information[extension]
        names = sorted(names)
        for name in names:
            file.write(name + '.' + extension + '\n')
        file.write('-' * 10 + '\n')
        number_max_unit = 0
        while size // 1024 > 0:
            size /= 1024
            number_max_unit += 1
        file.write(f'Summary: {round(size)} {list(UNITS.keys())[number_max_unit]}\n\n')

