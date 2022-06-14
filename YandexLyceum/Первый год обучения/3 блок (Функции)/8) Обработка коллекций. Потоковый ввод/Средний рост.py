import sys


heights = sys.stdin.readlines()
for i in range(len(heights)):
    heights[i] = int(heights[i].replace('\n', ''))
if heights:
    print(sum(heights) / len(heights))
else:
    print(-1)
