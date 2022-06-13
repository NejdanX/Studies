queue = []
count_event = int(input())
for i in range(count_event):
    event = input()
    if('встал' in event):
        if('встала' in event):
            event = event.replace("встала", "встал")
        queue.append(event.replace(" встал в очередь.", ''))  
    elif('за тобой' in event):
        event = event[8:]
        event = event.replace(" будет за тобой.", '')
        index_first_surname = event.find('!')
        first_surname = event[:index_first_surname]
        second_surname = event[index_first_surname + 2:]
        queue.insert(queue.index(first_surname) + 1, second_surname)
    elif('пошли' in event):
        queue.remove(event.replace(", хватит тут стоять, пошли отсюда.", ''))
for people in queue:
    print(people)