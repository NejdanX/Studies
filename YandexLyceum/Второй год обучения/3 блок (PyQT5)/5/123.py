def delilka(a):
    r = [a[g].lower() for g in range(len(a))]
    r.sort()
    return ''.join(r)


otv = {}
for i in range(int(input())):
    slovo = input().lower()
    slovo_razdel = delilka(slovo)
    if slovo_razdel in otv:
        otv[slovo_razdel].add(slovo)
    else:
        otv[slovo_razdel] = {slovo}
cash_000 = [sorted(value) for value in otv.values()]
for i in sorted(cash_000):
    print(*i)