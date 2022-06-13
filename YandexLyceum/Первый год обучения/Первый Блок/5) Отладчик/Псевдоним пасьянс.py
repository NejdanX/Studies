heap = int(input())
while heap != 0:
    take = int(input())
    if(take > 3 or take < 1 or take > heap):
        print(heap)
        continue
    heap -= take
    print(heap)