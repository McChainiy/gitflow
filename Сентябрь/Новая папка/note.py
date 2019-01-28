notes = {"ре": "ре-э", "до": "до-о", "ми": "ми-и", "фа": "фа-а",
         "соль": "со-оль", "ля": "ля-а", "си": "си-и"}

PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]


class Note:
    def __init__(self, nota, is_long=False):
        self.note = notes[nota] if is_long else nota

    def __str__(self):
        return self.note


class LoudNote(Note):
    def __str__(self):
        return self.note.upper()


class DefaultNote(Note):
    def __init__(self, nota='до', is_long=False):
        self.note = notes[nota] if is_long else nota


class NoteWithOctave(Note):
    def __init__(self, nota, octave, is_long=False):
        self.note = '{} ({})'.format(
            notes[nota], octave) if is_long else '{} ({})'.format(nota, octave)
