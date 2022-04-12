f = open("Hangman.txt", "r")
HangmanWord = (f.read())
f.close()

f = open("Hangman Graphics.py", "r")
f.read()
f.close()
from HangManGraphics import HangmanPics
lifecounter = len(HangmanPics)
Letters = list(HangmanWord)
DisplayList = []
WrongLetters = []
counter = 1
for i in Letters:
    DisplayList.append('_')


def WrongGuess(guess, j):
    if j == 0:
        global counter
        global WrongLetters
        global lifecounter
        WrongLetters.append(guess)
        print("You guessed the wrong letter")
        print("The letters that are not in the word are: " + str(WrongLetters))
        from HangManGraphics import HangmanPics
        print(HangmanPics[counter])
        counter = counter + 1
        lifecounter = lifecounter - 1
        if counter == 6:
            print("You lose! Better luck next time! ")
            exit(0)
        print("You have " + str(lifecounter) + " lives left.")

def LetterGuess():
    global Letters
    global counter
    global DisplayList
    BlanksCounter = 0
    guess = input("Please guess a letter: ")
    j = 0
    for i in Letters:
        if guess == i:
            j = 1
            DisplayList.pop(BlanksCounter)
            DisplayList.insert(BlanksCounter,guess)
            BlanksCounter = BlanksCounter +1
            print(DisplayList)
            print("You guessed a correct letter.")
            print(i)
        if '_' not in DisplayList:
            print("You win! Great job!")
            exit(0)
        else:
            BlanksCounter = BlanksCounter + 1
    WrongGuess(guess, j)


while True:
    LetterGuess()
