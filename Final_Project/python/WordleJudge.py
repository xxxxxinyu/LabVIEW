import string

class WordList:
    """
    Reads a list of words from a file and filters it for wordle compatible words.
    Used to provide word list copies.
    """

    def __init__(self, filename):
        self.ascii_lowercase = list(string.ascii_lowercase)
        with open(filename, encoding="utf8") as file:
            self.words = file.readlines()
            self.words = [word.rstrip() for word in self.words]
            self.words = [w for w in self.words if len(w) == 5 and self.is_ascii_lowercase(w)]
            self.words = list(dict.fromkeys(self.words))  # remove duplicates


    def get_list_copy(self):
        return self.words.copy()

    def is_ascii_lowercase(self, word):
        for letter in word:
            if letter not in self.ascii_lowercase:
                return False
        return True

class WordleJudge:
    """
    Helper class to take into account how common words are in the English language.
    """

    def __init__(self, words=WordList("C:/Users/xinyu/LabVIEW/Final_Project/data/combined_wordlist.txt").words,
                 common_words=WordList("C:/Users/xinyu/LabVIEW/Final_Project/data/common_words.txt").words):
        self.common_words = common_words
        self.probability = {}
        for word in words:
            self.probability[word] = self.__calculate_probability(word)

    def __calculate_probability(self, word):
        if word not in self.common_words:
            return 368 / (368 + 8890)
        relative_position = self.common_words.index(word) / len(self.common_words)
        return 0.85 * (1 - relative_position) + 0.35 * relative_position

    def is_wordle_probability(self, word):
        """
        :param word: a 5 letter word
        :return: the probability of the word being a wordle based on its popularity in the English language
        """
        return self.probability[word]