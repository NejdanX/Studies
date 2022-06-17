lucky_hours = sorted([hours for hours in input().split()], key=lambda x: int(x))
lucky_minutes = sorted([minutes for minutes in input().split()], key=lambda x: int(x))
for hours in lucky_hours:
    sum_digit_in_hours = int(hours[0]) + int(hours[1:] if hours[1:] else 0)
    for minutes in lucky_minutes:
        if sum_digit_in_hours != int(minutes[0]) + int(minutes[1:] if minutes[1:] else 0):
            print(f'{hours if len(hours) == 2 else "0" + hours}:{minutes if len(minutes) == 2 else "0" + minutes}')