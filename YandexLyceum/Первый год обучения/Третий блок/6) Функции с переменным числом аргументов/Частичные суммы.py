def partial_sums(*args):
    res = []
    for i in range(len(args) + 1):
        amount = 0
        for j in range(i):
            amount += args[j]
        res.append(amount)
    return res
