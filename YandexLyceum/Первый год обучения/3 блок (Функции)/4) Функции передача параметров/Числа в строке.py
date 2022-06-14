def from_string_to_list(string, container):
    c = string.split()
    for item in c:
        container.append(int(item))
