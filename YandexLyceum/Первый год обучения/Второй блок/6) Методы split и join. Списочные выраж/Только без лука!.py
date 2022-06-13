steps = int(input())
recipe = []
for i in range(steps):
    step = input()
    if('лук' not in step):
        recipe.append(step)
print(', '.join(recipe))