class LeftParagraph:
    def __init__(self, weight):
        self.words = []
        self.weight = weight

    def add_word(self, word):
        self.words.append(word)

    def end(self):
        while len(self.words) != 0:
            from_to_del = 0
            for i in range(1, len(self.words) + 1):
                string = ' '.join(self.words[:i])
                if len(string) > self.weight:
                    string = ' '.join(self.words[:i - 1])
                    from_to_del = i - 1
                    break
                from_to_del = i
            print(string.ljust(self.weight))
            for j in range(from_to_del):
                del self.words[0]


class RightParagraph:

    def __init__(self, weight):
        self.words = []
        self.weight = weight

    def add_word(self, word):
        self.words.append(word)

    def end(self):
        while len(self.words) != 0:
            from_to_del = 0
            for i in range(1, len(self.words) + 1):
                string = ' '.join(self.words[:i])
                if len(string) > self.weight:
                    string = ' '.join(self.words[:i - 1])
                    from_to_del = i - 1
                    break
                from_to_del = i
            print(string.rjust(self.weight))
            for j in range(from_to_del):
                del self.words[0]
