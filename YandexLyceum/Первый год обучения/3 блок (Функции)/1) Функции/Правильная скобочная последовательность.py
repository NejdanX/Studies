def bracket_check(test_string):
    open = 0
    close = 0
    isforced = False
    if not test_string:
        print('YES')
        return 0
    if test_string[0] == ')':
        print('NO')
        return 0
    for char in test_string:
        if char == '(':
            if open < close:
                print('NO')
                isforced = True
                break
            open += 1
        if char == ')':
            close += 1
    if close != open and not isforced:
        print('NO')
    elif not isforced:
        print('YES')