set_learn_english = set()
set_learn_german = set()
set_learn_french = set()
count_english = int(input())
count_german = int(input())
count_french = int(input())
count_learn_language = count_english + count_french + count_german
for i in range(count_learn_language):
    name = input()
    if(name not in set_learn_english):
        set_learn_english.add(name)
    elif(name not in set_learn_german):
        set_learn_german.add(name)
    elif(name not in set_learn_french):
        set_learn_french.add(name)
    else:
        set_learn_english.remove(name)
        set_learn_german.remove(name)
        set_learn_french.remove(name)
en_fr = (set_learn_english & set_learn_french) - set_learn_german
en_ge = (set_learn_english & set_learn_german) - set_learn_french
fr_ge = (set_learn_french & set_learn_german) - set_learn_english
count_people = len(en_fr) + len(en_ge) + len(fr_ge)
if(count_people == 0):
    print("NO")
else:
    print(count_people)
