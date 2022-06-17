N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
ALL_PITCHES = PITCHES + LONG_PITCHES
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


class Note:
    def __init__(self, note, is_long=False):
        self.is_long = is_long
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
            return Note(new_note, self.is_long)
        new_note = PITCHES[(PITCHES.index(self.note) + count_bit) % N]
        return Note(new_note, self.is_long)

    def __lshift__(self, count_bit):
        if self.is_long:
            new_note = LONG_PITCHES[(LONG_PITCHES.index(self.note) - count_bit) % N]
            return Note(new_note, self.is_long)
        new_note = PITCHES[(PITCHES.index(self.note) - count_bit) % N]
        return Note(new_note, self.is_long)


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


do = Note("до", True)
re = Note("ре", True)
mi = Note("ми", True)
fa = Note("фа", True)
sol = Note("соль", True)
la = Note("ля", True)
si = Note("си", True)

r1 = do >> 1
print(r1)
m1 = r1 >> 1
print(m1)
f1 = m1 >> 1
print(f1)
print()

sl1 = re >> 1 >> 2
print(sl1)
print()

d2 = si >> 1
m2 = d2 >> 2
print(m2)
mm2 = m2 >> 7
print(mm2)
r2 = mm2 >> 55
print(r2)
print()

nf = si << 3
print(nf)
nr = nf << 2
print(nr)
print()

nl2 = re << 3
print(nl2)
nsol = do << 73
print(nsol)
nm2 = mi << 21
print(nm2)
print()

nr = si << 2 << 1 << 2
print(nr)
nf = nr << 2 << 4 << 6
print(nf)