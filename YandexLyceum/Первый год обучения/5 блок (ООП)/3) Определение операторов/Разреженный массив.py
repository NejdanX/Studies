class SparseArray:
    def __init__(self):
        self.array = {}
        self.there_is = []

    def __getitem__(self, key):
        if key in self.array:
            return self.array[key]
        return 0

    def __setitem__(self, key, value):
        self.array[key] = value
        self.there_is.append(key)
