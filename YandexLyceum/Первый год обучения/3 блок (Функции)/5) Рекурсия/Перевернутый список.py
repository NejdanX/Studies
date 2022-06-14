def recursive_reverse(some_list):
    if not some_list:
        return []
    else:
        return [some_list.pop()] + recursive_reverse(some_list)


reversed_list = recursive_reverse([1, 2, 3])
print(*reversed_list)