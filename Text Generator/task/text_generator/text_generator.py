from collections import Counter, defaultdict
from random import choices, choice


class TextGenerator:

    def __init__(self, file_name):
        file = open(file_name, "r", encoding="utf-8")
        self.tokens = file.read().split()
        self.unique_tokens = set(self.tokens)
        self.pairs = defaultdict(Counter)
        for i in range(len(self.tokens) - 2):
            self.pairs[' '.join(self.tokens[i:i + 2])].update((self.tokens[i + 2],))

    def find_start(self):
        while True:
            start = choice(list(self.pairs)).split()
            if start[0].isalpha() and start[0].title() == start[0] and start[0][-1] not in '.!?':
                return start

    def make_pseudo_sentence_with_n_words(self, n=5):
        res = []
        while True:
            if len(res) == 0:
                res = self.find_start()
            current = ' '.join(res[-2:])
            next_word = choices(list(self.pairs[current].keys()), list(self.pairs[current].values()))[0]
            res.append(next_word)
            if next_word[-1] in '.!?':
                if len(res) < n:
                    res = []
                    continue
                return ' '.join(res)


def main():
    game_of_thrones = TextGenerator(input())
    for _ in range(10):
        print(game_of_thrones.make_pseudo_sentence_with_n_words())


if __name__ == '__main__':
    main()
