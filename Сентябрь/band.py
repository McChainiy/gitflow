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
