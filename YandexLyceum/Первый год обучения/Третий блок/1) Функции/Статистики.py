def median(arr):
    arr = sorted(arr)
    if len(arr) % 2 == 0:
        left_index = int(len(arr) / 2 - 0.5)
        right_index = int(len(arr) / 2 + 0.5)
        return (arr[left_index] + arr[right_index]) / 2
    else:
        return arr[int(len(arr) / 2 - 0.5)]


def average(arr):
    return sum(arr) / len(arr)


def print_statistics(arr):
    if arr:
        print(len(arr), average(arr), min(arr), max(arr), median(arr))
    else:
        print(0, 0, 0, 0, 0)
