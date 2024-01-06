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

# if __name__ == "__main__":
#     word = input("Enter word: ")
#     result = isLegal(word)
#     print(result)
