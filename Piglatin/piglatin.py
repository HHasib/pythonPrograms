#CIS 1051
#Abu Hasnat Hasib
#This program encodes a word into Pig Latin format
# The __main__ function is what executes the whole code integrating various functions to perform the job



def __main__():
    notDone = True  #at first x is assigned to to make a continuous loop

    while notDone :

        word = input("Enter a word: ")
        lowercase = word.lower()
        # print(lowercase)
        if lowercase == "done":   #if the computer detects done written it will set the value of x to False and thus the while loop stops
            return None
        y = findFirstVowel(lowercase)
        # print(y)
        print("PigLatin Format:",convertToPigLHatin(lowercase,y))
        print("Reversed:",reverse(word))
        print("ROT13 Encrypted:",ROT13(word))

def findFirstVowel(word):
    vowels = "aeiou"
    for i,char in enumerate(word):
        if char in vowels:
            return i        # vowels in last letter and no vowels results same
    return None



def convertToPigLHatin(word,vowelPosition):
    if vowelPosition == None:
        newWord = word
    elif vowelPosition == 0:
        newWord = word[1:]+word[0]+"way"
    else:
        newWord = word[vowelPosition:]+word[:vowelPosition]+"ay"

    return newWord

def reverse(word):
    newWord = ""
    for letters in range (-1, -(len(word))-1,-1):
        newWord += word[letters]
    return newWord

def ROT13(word):
    newWord = ""
    normal =    "abcdefghijklmnopqrstuvwxyz "
    encrypted = "nopqrstuvwxyzabcdefghijklm "
    for letters in word:
        pos = normal.index(letters)
        newWord += encrypted[pos]
    return newWord


__main__()