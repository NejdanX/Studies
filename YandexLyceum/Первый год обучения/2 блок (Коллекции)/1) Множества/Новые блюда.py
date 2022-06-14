all_meal = set()
cooked_meal = set()
for i in range(int(input())):
    all_meal.add(input())
for i in range(int(input())):
    for j in range(input()):
        cooked_meal.add(input())
not_cooked_meal = all_meal - cooked_meal
for meal in not_cooked_meal:
    print(meal)