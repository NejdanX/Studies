PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]


class Note:
    def __init__(self, note, is_long=False):
        self.note = note
        self.is_long = is_long
        self.long_notes = {'до': 'до-о', 'ре': 'ре-э', 'ми': 'ми-и', 'фа': 'фа-а',
                           'соль': 'со-оль', 'ля': 'ля-а', 'си': 'си-и'}

    def __str__(self):
        if self.is_long:
            return self.long_notes[self.note]
        return self.note


class LoudNote(Note):
    def __str__(self):
        if self.is_long:
            return self.long_notes[self.note].upper()
        return self.note.upper()


class DefaultNote(Note):
    def __init__(self, note='до', is_long=False):
        super().__init__(note, is_long)


class NoteWithOctave(Note):
    def __init__(self, note, octave, is_long=False):
        self.octave = octave
        super().__init__(note, is_long)

    def __str__(self):
        if self.is_long:
            return self.long_notes[self.note] + f' ({self.octave})'
        return self.note + f' ({self.octave})'


print(Note("соль"))

print(LoudNote(PITCHES[4]))
print(LoudNote("си", is_long=True))

print(DefaultNote("ми"))
print(DefaultNote())
print(DefaultNote(is_long=True))

print(NoteWithOctave("ре", "первая октава"))
print(NoteWithOctave("ля", "малая октава", is_long=True))