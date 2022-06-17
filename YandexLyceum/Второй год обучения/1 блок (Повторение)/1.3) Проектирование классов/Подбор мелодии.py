N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
ALL_PITCHES = PITCHES + LONG_PITCHES
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


class Note:
    def __init__(self, note, is_long=False, is_shift=False):
        self.is_long = is_long
        self.is_shift = is_shift
        if note in LONG_PITCHES:
            self.note = LONG_PITCHES[LONG_PITCHES.index(note)]
        elif is_long:
            self.note = LONG_PITCHES[PITCHES.index(note)]
        else:
            self.note = note

    def __str__(self):
        if self.is_long:
            return ALL_PITCHES[ALL_PITCHES.index(self.note)]
        return self.note

    def get_interval(self, other):
        s_note = self.note
        o_note = other.note
        if self.is_long:
            s_note = PITCHES[LONG_PITCHES.index(self.note)]
        if other.is_long:
            o_note = PITCHES[LONG_PITCHES.index(other.note)]
        return INTERVALS[abs(PITCHES.index(s_note) - PITCHES.index(o_note))]

    def __eq__(self, other):
        return ALL_PITCHES.index(self.note) % N == ALL_PITCHES.index(other.note) % N

    def __ne__(self, other):
        return ALL_PITCHES.index(self.note) % N != ALL_PITCHES.index(other.note) % N

    def __le__(self, other):
        return ALL_PITCHES.index(self.note) % N <= ALL_PITCHES.index(other.note) % N

    def __ge__(self, other):
        return ALL_PITCHES.index(self.note) % N >= ALL_PITCHES.index(other.note) % N

    def __lt__(self, other):
        return ALL_PITCHES.index(self.note) % N < ALL_PITCHES.index(other.note) % N

    def __gt__(self, other):
        return ALL_PITCHES.index(self.note) % N > ALL_PITCHES.index(other.note) % N

    def __rshift__(self, count_bit):
        if self.is_long:
            new_note = LONG_PITCHES[(LONG_PITCHES.index(self.note) + count_bit) % N]
            return Note(new_note, self.is_long, (LONG_PITCHES.index(self.note) + count_bit) > 6)
        new_note = PITCHES[(PITCHES.index(self.note) + count_bit) % N]
        return Note(new_note, self.is_long, (PITCHES.index(self.note) + count_bit) > 6)

    def __lshift__(self, count_bit):
        if self.is_long:
            new_note = LONG_PITCHES[(LONG_PITCHES.index(self.note) - count_bit) % N]
            return Note(new_note, self.is_long, (LONG_PITCHES.index(self.note) - count_bit) < 0)
        new_note = PITCHES[(PITCHES.index(self.note) - count_bit) % N]
        return Note(new_note, self.is_long, (PITCHES.index(self.note) - count_bit) < 0)


class LoudNote(Note):
    def __str__(self):
        if self.is_long:
            return LONG_PITCHES[PITCHES.index(self.note)].upper()
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
            return LONG_PITCHES[PITCHES.index(self.note)] + f' ({self.octave})'
        return self.note + f' ({self.octave})'


class Melody:
    def __init__(self, sequence_of_notes=list()):
        self.sequence_of_notes = sequence_of_notes[:]

    def __str__(self):
        result = [str(obj) for obj in self.sequence_of_notes]
        return ', '.join(result).capitalize()

    def __len__(self):
        return len(self.sequence_of_notes)

    def append(self, note):
        self.sequence_of_notes.append(note)

    def replace_last(self, note):
        self.sequence_of_notes[-1] = note

    def remove_last(self):
        self.sequence_of_notes.pop()

    def clear(self):
        self.sequence_of_notes.clear()

    def __rshift__(self, shift):
        result = []
        for obj in self.sequence_of_notes:
            changed_obj = obj >> shift
            result.append(changed_obj)
            if changed_obj.is_shift:
                return Melody(self.sequence_of_notes)
        return Melody(result)

    def __lshift__(self, shift):
        result = []
        for obj in self.sequence_of_notes:
            changed_obj = obj << shift
            result.append(changed_obj)
            if changed_obj.is_shift:
                return Melody(self.sequence_of_notes)
        return Melody(result)


melody = Melody([Note('ля'), Note('соль'), Note('ми'),  Note('до', True)])
print(melody)
print(Melody() >> 2)
melody_up = melody >> 1
melody_down = melody << 1
melody.replace_last(Note('соль'))
print('>> 1:', melody_up)
print('<< 1:', melody_down)
print(melody)
