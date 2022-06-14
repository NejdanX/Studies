# Привет, как тебя там?
def who_are_you_and_hello():
    while True:
        name = input()
        changed_name = ''.join(e for e in name if e.isalpha())
        changed_name = changed_name.capitalize()
        if(name == changed_name):
            print(f"Привет, {name}!")
            break

# Какая четверть?
def quarter(xcoord, ycoord):
    if(xcoord > 0 and ycoord > 0):
        print('I четверть')
    elif(xcoord < 0 and ycoord > 0):
        print('II четверть')
    elif(xcoord < 0 and ycoord < 0):
        print('III четверть')
    elif(xcoord > 0 and ycoord < 0):
        print('IV четверть')


# Формальное приветствие
def greet():
	name = input()
	surname = input()
	print(f"Здравствуйте, {name} {surname}.")


# Золотое сечение
def golden_ratio(i):
    previous = 0
    next = 1
    sum = 0
    for _ in range(i):
        sum = previous + next
        previous, next = next, sum
    print(next / previous)


def ask_password():