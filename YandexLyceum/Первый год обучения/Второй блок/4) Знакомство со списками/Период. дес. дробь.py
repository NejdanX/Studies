n = int(input())
first_pos = {}
position = 0
period = ""
remainder = 1
while not (remainder in first_pos):
    first_pos[remainder] = position
    period += str(remainder // n)
    remainder = (remainder % n) * 10
    position += 1
period = period[first_pos[remainder]:]
print(period)