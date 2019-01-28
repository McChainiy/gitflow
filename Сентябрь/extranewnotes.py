import copy
N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


class Note:
    def __init__(self, nota, is_long=False):
        self.height = PITCHES.index(nota)
        self.long = is_long
        self.note = LONG_PITCHES[self.height] if is_long else nota

    def __str__(self):
        return self.note

    def __lt__(self, y):
        return self.height < y.height

    def __le__(self, y):
        return self.height <= y.height

    def __eq__(self, y):
        return self.height == y.height

    def __ne__(self, y):
        return self.height != y.height

    def __gt__(self, y):
        return self.height > y.height

    def __ge__(self, y):
        return self.height >= y.height

    def __rshift__(self, y):
        return Note(PITCHES[(self.height + y) % 7], self.long)

    def __lshift__(self, y):
        return Note(PITCHES[(self.height - y) % 7], self.long)

    def get_interval(self, y):
        return INTERVALS[abs(self.height - y.height)]


class LoudNote(Note):
    def __str__(self):
        return self.note.upper()


class DefaultNote(Note):
    def __init__(self, nota='до', is_long=False):
        self.height = PITCHES.index(nota)
        self.note = LONG_PITCHES[self.height] if is_long else nota


class NoteWithOctave(Note):
    def __init__(self, nota, octave, is_long=False):
        self.height = PITCHES.index(nota)
        self.note = '{} ({})'.format(LONG_PITCHES[self.height],
                                     octave) if is_long else '{} ({})'.format(nota, octave)


class Melody:
    def __init__(self, notes=[]):
        self.notes = notes

    def __str__(self):
        tobe = []
        for i in self.notes:
            tobe.append(i.note)
        tobe = ', '.join(tobe)
        if len(tobe) == 0:
            return ''
        return tobe[0].upper() + tobe[1:]

    def append(self, note):
        self.notes.append(note)

    def remove_last(self):
        if len(self.notes) == 0:
            return
        del self.notes[-1]

    def replace_last(self, note):
        self.remove_last()
        self.append(note)

    def clear(self):
        self.notes = []

    def __len__(self):
        return len(self.notes)

    def __rshift__(self, y):
        new_melody = []
        for i in self.notes:
            if i.height + y not in range(7):
                return Melody(copy.deepcopy(self.notes))
            new_melody.append(i >> y)
        return Melody(new_melody)

    def __lshift__(self, y):
        new_melody = []
        for i in self.notes:
            if i.height - y not in range(7):
                return Melody(copy.deepcopy(self.notes))
            new_melody.append(i << y)
        return Melody(new_melody)


mel1 = Melody([Note('ре', True), Note('ми'), Note('до', True), Note('фа'), Note('ля'), Note('соль', True)])
m1 = mel1 >> 1
m2 = mel1 >> 3
print(m1)
print(m2)
print()

mel2 = Melody([Note('ре', True), Note('ми'), Note('до', True), Note('фа'), Note('ля'), Note('соль', True)])
m3 = mel2 << 2
m4 = mel2 << 2
print(m3)
print(m4)
print()

n1 = Note('фа', True)
n2 = Note('соль', True)
mel3 = Melody()
mel3.append(n1)
mel3.append(n2)
m5 = mel3 >> 1 >> 1
m6 = mel3 << 1 << 1
m7 = mel3 >> 3
m8 = mel3 << 3
print(m5)
print(m6)
print(m7)
print(m8)
print()

mel4 = Melody()
m9 = mel4 >> 3
m10 = mel4 << 3
print(m9)
print(m10)
print()

n3 = Note('ми', True)
n4 = Note('ми')
n5 = Note('фа')
mel5 = Melody([n5, n4, n3])
m11 = mel5 >> 2
m12 = mel5 << 2
m13 = mel5 >> 12
m14 = mel5 << 6
print(m11)
print(m12)
print(m13)
print(m14)