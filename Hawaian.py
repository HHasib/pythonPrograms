#Abu Hasnat Hasib
#CIS 1051

#valid character- a,e,i,o,u,p,k,h,l,m,n,w

def main():
    torf = True
    torf2 = False

    while torf == True:
        word = input("Enter a Hawaiian word to pronounce ==> ")
        word = word.lower()
        newWord = validity(word)
        if newWord == False:
            torf = False
            torf2 = True
        else:
            newWord = newWord.capitalize()
            word = word.upper()
            print (word, "is pronounced", newWord)
            torf2 = True



        while torf2 == True:
            response = input("Do you want to enter another word? Y/YES/N/NO ==> ")
            response = response.lower()
            if response == "yes" or response == "y":
                torf2 = False
                torf = True
            elif response == "no" or response == "n":
                torf2 = False
                torf = False
            else :
                print("Enter Y, Yes, N or No")
                torf2 = True



def validity(word):
    validLetters = "aeioupkhlmnw\' "

    for letter in word:
        if letter not in validLetters:
            letter = letter.upper()
            print("%s is not a valid Hawaiin character" % letter)
            return False

    return convert(word)



def convert(word):
    answer = ""
    i = 0

    while i < len(word):

        letter = word[i]
        if i < len(word)-1:
            nextLetter = word[i+1]
        elif i == len(word)-1:
            nextLetter = ""
        if i > 0:
            prevLetter = word[i-1]

        # if word[0] == "w":
        #     answer += "w"
        if letter == "w" and word.index(letter) != 0:
            if prevLetter == "i" or prevLetter == "e":
                answer += "v"
            else:
                answer += "w"
        elif letter == "a":
            if nextLetter == "i" or nextLetter == "e":
                answer += "eye"
                i+=1
            elif nextLetter == "o" or nextLetter == "u":
                answer += "ow"
                i+=1
            else:
                answer += "ah"

        elif letter == "e":
            if nextLetter == "i":
                answer += "ay"
                i+=1
            elif nextLetter == "u":
                answer += "eh-oo"
                i+=1

            else:
                answer += "eh"
        elif letter == "i":
            if nextLetter == "u":
                answer += "ew"
                i+=1

            else:
                answer += "ee"
        elif letter == "o":
            if nextLetter == "i":
                answer += "oyo"
                i+=1
            elif nextLetter == "u":
                answer += "ow"
                i+=1
            else:
                answer += "oh"
        elif letter == "u":
            if nextLetter == "i":
                answer += "ooey"
                i+=1
            else:
                answer += "oo"

        else:
            answer += letter
        if letter in "aeiou" and i != len(word)-1 and nextLetter !=" " and nextLetter != "\'" :
            answer += "-"

        i+=1
    return answer

main()
