from OutcomeBasedAI import OutcomeBasedAI
from randomAns import randomAns
from LetterInformation import LetterInformation

def isLegal(word, filename):
    #filename = "C:/Users/xinyu/LabVIEW/Final_Project/data/official_allowed_guesses.txt"

    with open(filename, encoding="utf8") as file:
        legalWords = file.readlines()
        legalWords = [word.rstrip() for word in legalWords]
        legalWords = [w for w in legalWords if len(w) == 5]
        legalWords = list(dict.fromkeys(legalWords))  # remove duplicates

    word = word.lower()
    if word in legalWords: 
        return True
    return False


def play(competitor, filename, word):
    guesses = []
    success = False
    guess_history = []

    for i in range(6):  # Up to 6 guesses
        guess = competitor.guess(guess_history)
        print("guess: ", guess)
        if not isLegal(guess, filename):
            # print("Competitor ", competitor.__class__.__name__, " is a dirty cheater!")
            # print("hard_mode: ", self.hard_mode, "guess: ", guess, "guess_history", guess_history)
            print("Competition aborted.")
            quit()

        guess_result = []
        for c in range(5):
            if guess[c] not in word:
                guess_result.append(LetterInformation.NOT_PRESENT)
            elif word[c] == guess[c]:
                guess_result.append(LetterInformation.CORRECT)
            else:
                guess_result.append(LetterInformation.PRESENT)
        guess_history.append((guess, guess_result))
        guesses.append(guess)

        if guess == word:
            success = True
            break
    return success, guesses

def AI(ans):
    filename = "C:/Users/xinyu/LabVIEW/Final_Project/data/common_words.txt"
    legalWord_filename = "C:/Users/xinyu/LabVIEW/Final_Project/data/combined_wordlist.txt"
    competitor = OutcomeBasedAI()

    print("answer: ", ans)
    ans = ans.lower()
    success, guesses = play(competitor, legalWord_filename, ans)
    print("success: ", success, "guesses: ", guesses)

    for i in range(len(guesses)):
        guesses[i] = " " + guesses[i].upper()
        
    return guesses
    

# if __name__ == "__main__":
#     AI("hello")