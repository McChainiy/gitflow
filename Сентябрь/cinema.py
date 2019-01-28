import copy


def convert_time(time):
    return tuple([int(i) for i in time.split(':')])


class Cinema:
    def __init__(self):
        self.halls = {}

    def append(self, hall):
        self.halls[len(self.halls) + 1] = hall

    def get_movie(self, name):
        times = {}
        for i in self.halls.keys():
            if name in self.halls[i].movies.keys():
                times[i] = self.halls[i].movies[name]
        return times


class Hall:
    def __init__(self, config, number=42):
        self.number = number
        self.schedule = {}
        self.movies = {}
        self.config = [['-' for i in range(config[1])] for i in range(config[0])]

    def append(self, movie, time):
        places = copy.deepcopy(self.config)
        self.schedule[time] = (movie, places)
        self.movies[movie.name] = self.movies.get(movie.name, []) + [time]

    def print_config(self, time):
        for i in self.schedule[time][1]:
            print(i)

    def buy_seat(self, time, seat):
        seat = [int(i) for i in seat.split(' ')]
        if self.schedule[time][1][seat[0] - 1][seat[1] - 1] == '+':
            return False
        self.schedule[time][1][seat[0] - 1][seat[1] - 1] = '+'
        return True


class Movie:
    def __init__(self, name, duration, *info):
        self.name = name
        self.duration = duration
        self.info = info if len(info) > 0 else '-'

    def inform(self):
        return 'Длительность - {}\nОписание - {}'.format(self.duration, *self.info)


cinemas = {}
movies = {}

while not False:
    command = input('Введите команду: ')
    if command == 'create cinema':
        while not False:
            name = input('Введите название кинотетра: ')
            if name in cinemas.keys():
                print('Кинотеатр с таким названием уже есть. Попробуйте еще раз')
                continue
            else:
                cinemas[name] = Cinema()
                print('Кинотеатр {} занесен в реестр'.format(name))
                break
    elif command == 'create hall':
        while not False:
            try:
                cinema = input('Введите кинотеaтр: ')
                conf = input('Введите конфигурацию в формате (x y), '
                             'где x - кол-во рядов, а у - кол-во столбцов: ')
                cinemas[cinema].append(Hall([int(i) for i in conf.split()]))
                print('В кинотеатре {} появился {}-ый зал с конфигурацией кресел {}'.format(
                    cinema, len(cinemas[cinema].halls), conf))
                break
            except TypeError:
                print('Ошибка при вводе данных')
    elif command == 'create movie':
        while not False:
            try:
                name = input('Введите название фильма: ')
                if name in cinemas.keys():
                    print('Фильм с таким названием уже есть. Попробуйте еще раз')
                    continue
                dur = input('Введите длительность в формате часы:минуты : ')
                if len(dur.split(':')) < 2 or not(dur.replace(':', '').isdigit()):
                    raise TypeError
                inf = input('Введите описание (необязательно): ')
                movies[name] = Movie(name, dur, inf)
                print('Фильм {} занесен в реестр'.format(name))
                break
            except TypeError:
                print('Некорректная длисетльность')
                break
            except TypeError:
                print('Неправильные данные')
                break
    elif command == 'create session':
        try:
            cinema_name = input('Введите название кинотеатра: ')
            hall_num = input('Введите номер зала: ')
            movie_name = input('Введите название фильма: ')
            movie_time = input('Введите время начала фильма: ')
            cinemas[cinema_name].halls[int(hall_num)].append(movies[movie_name], movie_time)
        except TypeError:
            print('Ошибка в данных')
    elif command == 'movie time':
        try:
            movie_name = input('Введите название фильма: ')
            cinema_name = input('Введите название кинотеатра: ')
            print('В кинотеатре {} фильм {} проходит в залах:'.format(cinema_name, movie_name))
            times = cinemas[cinema_name].get_movie(movie_name)
            if len(times) == 0:
                print('Фильм {} не идет в нашем кинотетре'.format(movie_name))
                break
            for i in times:
                print('Зал {} -'.format(i), *sorted(times[i]))

        except TypeError:
            print('Ошибка в данных')
    elif command == 'buy':
        try:
            cinema = input('Введите кинотеатр: ')
            hall = input('Введите номер зала: ')
            time = input('Введите время начала сеанса: ')
            cinemas[cinema].halls[int(hall)].print_config(time)
            seat = input('Введите место, которое хотите купить: ')
            if cinemas[cinema].halls[int(hall)].buy_seat(time, seat):
                print('Место номер {} ряд {} на сеанс в {} куплено'.format(seat.split()[1],
                                                                           seat.split()[0], time))
            else:
                print('Данное место занято')
            cinemas[cinema].halls[int(hall)].print_config(time)
        except TypeError:
            print('Ошибка в данных')
    elif command == 'inform':
        movie = input('Введите название фильма: ')
        if movie not in movies:
            print('Такого фильма нет')
            break
        print(movies[movie].inform())
    elif command == 'help':
        print('create cinema - создание кинотеатра\ncreate hall - создание зала')
        print('create movie - cоздание фильма\ncreate session - добавление сеанса фильма в зал')
        print('movie time - все сеансы фильма\nbuy - купить место на сеанс\ninform - инфа о фильме')
    else:
        print('Такой команды нет. Help для справки')