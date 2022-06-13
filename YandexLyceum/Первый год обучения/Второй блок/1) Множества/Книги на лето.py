set_have_book = set()
count_have = int(input())
count_read = int(input())
for i in range(count_have):
    set_have_book.add(input())
for i in range(count_read):
    if(input() in set_have_book):
        print("YES")
    else:
        print("NO")