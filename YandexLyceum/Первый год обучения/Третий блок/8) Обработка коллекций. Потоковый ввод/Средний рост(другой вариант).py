def main():
    amount = 0
    count = 0
    try:
        a = input()
    except EOFError:
        print(-1)
        return
    while a != '^D':
        amount += int(a)
        count += 1
        try:
            a = input()
        except EOFError:
            break

    if count:
        print(amount / count)
    else:
        print(-1)

main()