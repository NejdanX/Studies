import sys
for line in sys.stdin:
    if line == '\n':
        break
    print(line.rstrip('\n'))
#str_data = sys.stdin.readlines()
#for i in range(len(str_data)):
   # str_data[i] = str_data[i].replace('\n', '')
#print(str_data)