import datetime as dt
films_with_session = {}

class Cinema:
    def __init__(self, name, halls=[]):
        self.name = name
        self.halls = halls[:]

    def append(self, hall):
        self.halls.append(hall)

    def delete(self, hall):
        del self.halls[self.halls.index(hall)]

    def clear(self):
        self.halls.clear()

    def __str__(self):
        halls = ', '.join([hall.hall_number for hall in self.halls])
        return 'Кинотеатр: {0}\nДоступные залы: {1}'.format(self.name, halls)


class CinemaHall:
    def __init__(self, hall_number, count_seat=(10, 10), films=[], from_left_to_right=False):
        self.hall_number = hall_number
        self.rows, self.cols = count_seat
        self.order = from_left_to_right
        self.films = films[:]
        self.seats = {'{0}{1}'.format(i + 1, j + 1): True for i in range(self.rows) for j in range(self.cols)}

    def __repr__(self):
        return self.hall_number

    def __str__(self):
        result = ''
        if self.order:
            for i in range(1, self.rows + 1):
                result += f'Row: {i}\t* '
                for j in range(self.cols, 0, -1):
                    result += '[{0} {1}] '.format(j, self.seats[str(i) + str(j)])
                result += '\n'
        else:
            for i in range(1, self.rows + 1):
                result += f'Row: {i}\t* '
                for j in range(1, self.cols + 1):
                    result += '[{0} {1}] '.format(j, self.seats[str(i) + str(j)])
                result += '\n'
        return 'Зал: {0}\n{1}'.format(self.hall_number, result)

    def is_seat_exist(self, seat):
        row, col = seat.split()[1], seat.split()[-1]
        if int(row) > self.rows or int(col) > self.cols:
            return False
        return True

    def is_seat_free(self, seat):
        row, col = seat.split()[1], seat.split()[-1]
        if self.is_seat_exist(seat):
            return True if self.seats[row + col] else False
        return 'Не существует'

    def seats_in_row(self, count):
        seats = []
        if count > self.cols:
            return []
        for i in range(1, self.rows + 1):
            seats.clear()
            counter = 0
            for j in range(1, self.cols + 1):
                seat = self.seats[str(i) + str(j)]
                if seat:
                    counter += 1
                    seats.append(str(i) + str(j))
                    if counter == count:
                        return seats
                else:
                    counter = 0
                    seats.clear()
        print('В зале {0} нет такого количества свободных мест в один ряд'.format(self.hall_number))
        return []

    def append(self, film):
        self.films.append(film)

    def insert(self, film, index):
        self.films.insert(film, index)

    def delete(self, film):
        del self.films[self.films.index(film)]

    def clear(self):
        self.films.clear()


class Film:
    def __init__(self, film, session='00:00-00:00'):
        self.film = film
        self.begin, self.end = session.split('-')[0], session.split('-')[1]

    def nearby_session(self, film):
        pass


class Ticket:
    def __init__(self, cinema, hall, film='', seat='Row: 1 Seat: 1'):
        self.cinema = cinema
        self.hall_init(hall)
        self.film_init(film)
        self.seat_init(seat)

    def hall_init(self, hall):
        helping = self.cinema.halls
        self.hall = [helping[i] for i in range(len(helping)) if hall == helping[i].hall_number]
        if self.hall:
            self.hall = self.hall[0]
        else:
            self.hall = CinemaHall('Не определен')
            print('Такого зала не существует')

    def film_init(self, film):
        helping = self.hall.films
        self.film = [helping[i] for i in range(len(helping)) if film == helping[i].film]
        if self.film:
            self.film = self.film[0]
        else:
            self.film = Film('Не определен')
            print('Такой фильм не идёт в данном зале')

    def seat_init(self, seat):
        if self.hall.is_seat_exist(seat) and self.hall.hall_number != 'Не определен' and \
                self.film.film != 'Не определен':
            self.seat = seat
            self.buy(seat)
        else:
            self.seat = 'Row: 1 Seat: 1'
            print('Не удалось купить билет на указанное место')

    def buy(self, seat):
        is_free = self.hall.is_seat_free(seat)
        row, col = seat.split()[1], seat.split()[-1]
        if is_free == 'Не существует':
            print('В зале {} нет такого места'.format(self.hall.hall_number))
        if is_free:
            self.hall.seats[row + col] = False
        elif not is_free:
            print('Это место уже занято')

    def __str__(self):  # Информация о билете
        row, col = self.seat.split()[1], self.seat.split()[-1]
        tab = '\t'
        result = '-' * 38 + '\n'
        result += f'{tab * 4}' + 'Билет' + '\n'
        result += f'  Зал: {self.hall.hall_number}\t\tРяд {row} Место {col}\n'
        result += f'  Фильм: {self.film.film}\n'
        result += f'  Время: {self.film.begin}\n'
        result += f'  Оплачен: {not(self.hall.is_seat_free(self.seat))}\n'
        result += '-' * 38 + '\n'
        return result


Cin = Cinema('Ocean', [CinemaHall('Hall 1', (5, 10)), CinemaHall('Hall 2', (10, 10), [Film('Cool')])])
tic = Ticket(Cin, 'Hall 1', 'Cool')
hall = 'Hall 2'
film = 'Cool'
print(Cin.halls[1].seats_in_row(10))
print(tic)