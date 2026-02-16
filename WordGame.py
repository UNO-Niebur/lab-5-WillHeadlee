#WordGame.py
#Name: William Headlee
#Date: 2/16/26
#Assignment: Lab 5

#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    for i in word:
        if i == letter:
            return True
    return False

def inSpot(letter, word, spot):
    if letter == word[spot]:
        return True
    return False

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""

    todayWord = word
    ratedGuess = ""
    spot = 0

    for letter in myGuess:
        if inSpot(letter, todayWord, spot):
            ratedGuess += myGuess[spot].upper()
        elif inWord(letter, todayWord):
            ratedGuess += myGuess[spot].lower()
        else:
            ratedGuess += "*"
        spot += 1

    return ratedGuess


def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    #print(todayWord)

    #User should get 6 guesses to guess
    guesses = 6

    #Ask user for their guess
    while guesses > 0:
        guess = ""
        while len(guess) != 5:
            guess = input("Guess a 5 letter word: ")
        if guess.lower() == todayWord.lower():
            print("You got it!")
            break

        #Give feedback using on their word:
        print(rateGuess(guess, todayWord))
        guesses -= 1
        print("You have " + str(guesses) + " guesses left")
    print("The word was " + todayWord)


if __name__ == '__main__':
  main()
