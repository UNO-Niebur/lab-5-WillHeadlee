#LetterFrequency.py
#Name: William Headlee
#Date: 2/16/26
#Assignment: Lab 5

#This program will create a CSV file of frequencies based on a text file.
#Use Excel or similar spreadsheet software to visualize the frequencies of the CSV file.

import os

def countLetters(message):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    message = message.lower()
    message = message.replace(" ", "")

    freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    #loop through each letter
    for ch in message:
        #Find the position in the alphabet
        alpha.find(ch) >= 0
        spot = (alpha.find(ch)) % 26
        #Increase the frequency at that position. If position was 5, then frequencies[5] = frequencies[5] + 1
        freq[spot] = freq[spot] + 1

    #Create the output text in the format A,5\n if there were 5 letter A in the message.
    #Remember that the \n is the symbol for a new line.
    output = ""
    for i in range(26):
        print (alpha[i], ":", freq[i])
        line = alpha[i] + "," + str(freq[i]) + "\n"
        output = output + line

    writeToFile(output)


def writeToFile(fileText):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    freqFile = open("frq.csv", 'w')
    freqFile.write(fileText)

    freqFile.close()


def main():
    msg = input("Enter a message: ")
    countLetters(msg)



if __name__ == '__main__':
  main()
