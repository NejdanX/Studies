def late(now, classes, bus):
    now = int(now.split(':')[0]) * 60 + int(now.split(':')[1])
    classes = int(classes.split(':')[0]) * 60 + int(classes.split(':')[1])
    if classes >= now + 20:
        i = 0
        while i != len(bus):
            if bus[i] < 5:
                del bus[i]
                i -= 1
                continue
            i += 1

        for _ in range(len(bus)):
            maximum = max(bus)
            del bus[bus.index(maximum)]
            if now + 15 + maximum <= classes:
                return f'Выйти через {maximum - 5} минут'
        return 'Опоздание'
    else:
        return 'Опоздание'
