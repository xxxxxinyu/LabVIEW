import os
import time
import string
import numpy as np

from enum import Enum, auto
from WordleJudge import WordleJudge
from LetterInformation import LetterInformation

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


class OutcomeBasedAI():
    """
    This AI calculates outcomes for every possible guess word.
    An outcome is calculated by the number of remaining options adjusted for the probability of the options being
    a wordle (based on how common the word is in the English language).

    For the first 3 guesses it chooses the option with the lowest mean outcome. This maximizes information gain.

    For any further guesses it switches to a MinMax strategy, using the guess with the best worst-outcome.

    The AI improves performance by precalculating the first 3 guesses.

    """

    def __init__(self):
        self.wordlist = WordList('C:/Users/xinyu/LabVIEW/Final_Project/data/combined_wordlist.txt')
        self.words = self.wordlist.get_list_copy()
        self.word_index = {k: v for v, k in enumerate(self.words)}
        self.judge = WordleJudge(self.words)

        data_path = 'C:/Users/xinyu/LabVIEW/Final_Project/data/'
        os.makedirs(data_path, exist_ok=True)
        guesses_filename = data_path + 'precalculated_guesses.npz'

        if not os.path.isfile(guesses_filename):
            self.precalculate_guesses(guesses_filename)
        self.precalculated_guesses = np.load(guesses_filename)

    def guess(self, guess_history):
        attempts = len(guess_history)
        if attempts == 0:  # precalculated
            return str(self.precalculated_guesses['first_guess'])
        if attempts == 1:  # precalculated
            return self.precalculated_guesses['second_guesses'][entry_info_to_outcome_id(guess_history[0][1])]
        if attempts == 2:  # precalculated
            return self.precalculated_guesses['third_guesses'][
                entry_info_to_outcome_id(guess_history[0][1]), entry_info_to_outcome_id(guess_history[1][1])]

        options = remaining_options(self.words, guess_history)
        if len(options) == 1:
            return options[0]  # solution found
        
        options_probability = [self.judge.is_wordle_probability(option) for option in options]
        if attempts == 5:  # last guess
            return options[options_probability.index(max(options_probability))]  # return best option

        w = 0
        best_worst_outcome = len(options)
        best_word = self.words[0]
        outcomes = np.empty(243, dtype=float)
        for i in range(len(self.words)):
            word = self.words[i]
            outcomes.fill(0)
            for option in options:
                outcome_id = calculate_outcome(word, option)
                outcomes[outcome_id] += self.judge.is_wordle_probability(option)
                if outcomes[outcome_id] > best_worst_outcome:
                    break
            outcomes[242] = 0  # don't punish for finding a solution
            worst_outcome = np.max(outcomes)
            if worst_outcome < best_worst_outcome or (worst_outcome == best_worst_outcome and (
                    best_word not in options or self.judge.is_wordle_probability(
                    word) > self.judge.is_wordle_probability(best_word)) and word in options):
                best_worst_outcome = worst_outcome
                best_word = word
            w += 1

        return best_word

    def precalculate_guesses(self, filename):
        print("Guesses file not found. Start precalculating guesses")
        start = time.time()
        print("Calculate first guess")
        first_guess = self.mean_outcome_guess(self.words, [], print_details=True)
        second_guesses = np.empty(243, dtype="<U5")
        third_guesses = np.empty((243, 243), dtype="<U5")
        print("\nCalculate guesses 2 and 3")
        for i in range(243):
            print("\routcome", i + 1, "/", 243, end="")
            guess_history_2 = [(first_guess, outcome_id_to_entry_info(i))]
            second_guesses[i] = self.mean_outcome_guess(self.words, guess_history_2)
            for j in range(243):
                if len(second_guesses[i]) == 5:
                    guess_history_3 = guess_history_2 + [(second_guesses[i], outcome_id_to_entry_info(j))]
                    third_guesses[i, j] = self.mean_outcome_guess(self.words, guess_history_3)
        np.savez(filename, first_guess=first_guess, second_guesses=second_guesses, third_guesses=third_guesses)
        # print("\nFinished precalculating guesses in ", time.time() - start, "seconds")

    def mean_outcome_guess(self, words, guess_history, print_details=False):
        options = remaining_options(words, guess_history)
        if len(options) == 0:
            return ""
        outcomes = np.zeros((len(words), 243))
        for w in range(len(words)):
            i = self.word_index[words[w]]
            if print_details:
                print("\rword", w + 1, "/", len(words), end="")
            for option in options:
                outcomes[i, calculate_outcome(words[w], option)] += self.judge.is_wordle_probability(option)
        outcomes[:, 242] = 0  # don't punish for finding a solution
        non_zero_mean = np.zeros(len(words))
        for i in range(len(words)):
            non_zero_outcomes = outcomes[i, np.nonzero(outcomes[i, :])]
            if non_zero_outcomes.size > 0:
                non_zero_mean[i] = non_zero_outcomes.mean()
        return words[non_zero_mean.argmin()]


def remaining_options(words, guess_history):
    """
    Filters a word list with all the known information.
    Returns the list of remaining options.
    """
    present = set()
    not_present = set()
    correct = set()
    present_letters = set()
    for entry in guess_history:
        for i in range(5):
            if entry[1][i] == LetterInformation.CORRECT:
                correct.add((entry[0][i], i))
                present_letters.add(entry[0][i])
            elif entry[1][i] == LetterInformation.PRESENT:
                present.add((entry[0][i], i))
                present_letters.add(entry[0][i])
            else:
                not_present.add(entry[0][i])
    
    for c in present_letters:
        words = [w for w in words if c in w]
    for c in not_present:
        words = [w for w in words if c not in w]
    for c in correct:
        words = [w for w in words if w[c[1]] == c[0]]
    for c in present:
        words = [w for w in words if w[c[1]] != c[0]]

    return words


def calculate_outcome(guess, solution):
    outcome = 0
    for i in range(5):
        if guess[i] == solution[i]:
            outcome += 2 * 3 ** i
        elif guess[i] not in solution:
            outcome += 3 ** i
    return outcome  # outcome id (0-242)


def entry_info_to_outcome_id(entry):
    o = 0
    for i in range(5):
        o += 3 ** i * (entry[i].value - 2)
    return o  # outcome id (0-242)


def outcome_id_to_entry_info(o):
    entry = []
    for i in range(5):
        entry.append(LetterInformation(((o // (3 ** i)) % 3) + 2))
    return entry
