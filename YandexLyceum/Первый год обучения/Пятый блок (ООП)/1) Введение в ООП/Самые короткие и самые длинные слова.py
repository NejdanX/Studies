class MinMaxWordFinder:
    def __init__(self):
        self.words = []

    def add_sentence(self, sentence):
        self.words += (x.strip('\t ') for x in sentence.split())
        self.words = sorted(self.words, key=lambda x: len(x))

    def shortest_words(self):
        if not self.words:
            return []
        min_length = len(self.words[0])
        return sorted(list(filter(lambda x: len(x) == min_length, self.words)))

    def longest_words(self):
        if not self.words:
            return []
        max_length = len(self.words[len(self.words) - 1])
        longest = list(set(self.words))
        return sorted(list(filter(lambda x: len(x) == max_length, longest)))
