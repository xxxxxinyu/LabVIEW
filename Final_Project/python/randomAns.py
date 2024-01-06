import random

def randomAns(filename):
    #filename = "C:/Users/xinyu/LabVIEW/Final_Project/data/sgb-words.txt"

    with open(filename, encoding="utf8") as file:
        legalWords = file.readlines()
        legalWords = [word.rstrip() for word in legalWords]
        legalWords = [w for w in legalWords if len(w) == 5]
        legalWords = list(dict.fromkeys(legalWords))  # remove duplicates
        
    index = random.randint(1, 5757)
    word = legalWords[index]
    word = word.upper()

    return word
    
# if __name__ == "__main__":
#     print(randomAns())