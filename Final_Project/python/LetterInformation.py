from enum import Enum, auto

class LetterInformation(Enum):
    UNKOWN = auto()  # light grey in the game
    PRESENT = auto()  # yellow in the game
    NOT_PRESENT = auto()  # dark grey in the game
    CORRECT = auto()  # green in the game