class ReversedList:
    def __init__(self, lst):
        self.lst = lst

    def __getitem__(self, key):
        return self.lst[(-key - 1)]

    def __len__(self):
        return len(self.lst)
