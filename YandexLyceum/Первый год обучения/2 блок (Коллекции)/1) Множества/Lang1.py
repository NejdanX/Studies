set_learn_english = set()
set_learn_german = set()
count_english = int(input())
count_german = int(input())
for i in range(count_english):
    name = input()
    if(name in set_learn_english):
        set_learn_english.remove(name)
        continue
    set_learn_english.add(name)
for i in range(count_german):
    name = input()
    if(name in set_learn_german):
        set_learn_german.remove(name)
        continue    
    set_learn_german.add(name)
set_only_one = set_learn_english ^ set_learn_german
if(len(set_only_one) == 0):
    print("NO")
else:
    print(len(set_only_one))