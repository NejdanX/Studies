white_list_size = int(input())
white_list = []
for i in range(white_list_size):
    white_list.append(input())
    
for i in range(int(input())):
    request = input()
    if(request in white_list):
        print(request)