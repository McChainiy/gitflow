from itertools import product


class Bell:
    def __init__(self, *args, **info):
        self.unnamed = args
        self.ding = True
        self.named = info

    def print_info(self):
        if self.unnamed == () and self.named == {}:
            print('-')
            return
        count = 0
        ending = ', '
        for i in sorted(self.named.keys()):
            if count == len(sorted(self.named.keys())) - 1:
                if self.unnamed == ():
                    ending = '\n'
                else:
                    ending = '; '
            print('{}: {}'.format(i, self.named[i]), end=ending)
            count += 1
        count = 0
        for i in self.unnamed:
            ending = '\n' if count == len(self.unnamed) - 1 else ', '
            print(i, end=ending)
            count += 1


class LittleBell(Bell):
    def sound(self):
        print('ding')


class BigBell(Bell):
    def sound(self):
        print('ding') if self.ding else print('dong')
        self.ding = not self.ding


class BellTower:
    def __init__(self, *bells):
        self.bells = list(bells)

    def sound(self):
        for i in self.bells:
            i.sound()
        print('...')

    def append(self, bell):
        self.bells.append(bell)

    def print_info(self):
        for i in range(len(self.bells)):
            print(i + 1, type(self.bells[i]).__name__)
            self.bells[i].print_info()
        print()


class SizedBellTower(BellTower):
    def __init__(self, *bells, size=10):
        self.bells = list(bells)
        self.size = size
        self.get_tostandart()

    def append(self, bell):
        if len(self.bells) < self.size:
            self.bells.append(bell)
        else:
            del self.bells[0]
            self.bells.append(bell)

    def get_tostandart(self):
        if len(self.bells) <= self.size:
            return
        self.bells = self.bells[(len(self.bells) - self.size):]


class TypedBellTower(BellTower):
    def __init__(self, *bells, bell_type=LittleBell):
        self.bells = bells
        self.type = bell_type
        self.get_tostandart()

    def append(self, bell):
        if type(bell) == self.type:
            self.bells.append(bell)

    def get_tostandart(self):
        self.bells = list(filter(lambda x: type(x) == self.type, self.bells))
