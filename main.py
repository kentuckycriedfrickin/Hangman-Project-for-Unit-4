f = open("Hangman.txt", "r")
HangmanWord = (f.read())  #  This reads the word so that the main program can use it later
f.close()

f = open("Hangman Graphics.py", "r") #Hangman Graphics is where I store the list of the graphics I use
f.read()
f.close()
from HangManGraphics import HangmanPics   # HangmanPics is the name of the list of graphics
lifecounter = len(HangmanPics)  #  The number of lives is equal to the number of hangman graphics I have
Letters = list(HangmanWord)    # The letters are equal to the list of letters in the word
DisplayList = [] 
WrongLetters = []
counter = 1  # This exists because it makes it so that another variable doesn't loop over and over
for i in Letters:
    DisplayList.append('_')  # This replaces the letters in the word with blanks


def WrongGuess(guess, j):   # This is the function for when the guess is wrong
    if j == 0:
        global counter
        global WrongLetters
        global lifecounter
        WrongLetters.append(guess)    # this adds the wrong letters to a list that will be displayed to the player
        print("You guessed the wrong letter")
        print("The letters that are not in the word are: " + str(WrongLetters))
        from HangManGraphics import HangmanPics
        print(HangmanPics[counter])  # this prints the item on the list that is equal to what counter is
        counter = counter + 1
        lifecounter = lifecounter - 1  
        if counter == 6:    # Lose factor
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
    for i in Letters:  # for any letter in the word
        if guess == i:  # If the guess is equal to any of the letters in the word...
            j = 1
            DisplayList.pop(BlanksCounter)  
            DisplayList.insert(BlanksCounter,guess)  # Basically inserts the letter into the blank
            BlanksCounter = BlanksCounter +1
            print(DisplayList)
            print("You guessed a correct letter.")
            print(i)
        if '_' not in DisplayList:   # basically when all the blanks are filled, you win
            print("You win! Great job!")
            exit(0)
        else:
            BlanksCounter = BlanksCounter + 1
    WrongGuess(guess, j) # if it's wrong we go to the wrongguess function


while True:
    LetterGuess()  # basically its supposed to loop letterguess until you win or lose
