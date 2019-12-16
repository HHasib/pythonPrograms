# Name: Abu Hasnat Hasib
#CIS 1051
#Professor Andrew B. Rosen

import re

def regexDictionary():
    #All regex
    catDogRegex = re.compile(r'(cat)|(dog)')
    fourLetterRegex = re.compile(r'^[A-z]{4}$')
    hunRegex = re.compile(r'hun')
    INGRegex = re.compile(r'ing$')
    IONRegex = re.compile(r'ion$')
    notQURegex = re.compile(r'q[^u]')
    noVowelRegex = re.compile(r'[aeiouAEIOU]')
    onlyVowelsRegex = re.compile(r'^[AEIOUaeiou]*$')
    endingwithNOTRegex = re.compile(r'(\'nt)$')
    twoVowelsrowRegex = re.compile(r'[aeiouAEIOU]{2}')
    twoVowelsRegex = re.compile(r'[aeiouAEIOU].*[aeiouAEIOU]')

    values = {'contain cat or dog':0, 'contain four letters':0, 'contain \'hun\'':0, 'end with \'ing\'':0, 'end with \'ion\'':0,
              'contain a \'q\' not immediately followed by a \'u\'':0, 'contain no vowels':0, 'contain only vowels':0,
              'end with \"\'nt\"':0, 'contain two vowels in a row':0, 'contain at least two vowels':0}

    data = open('words.txt', 'r')
    for word in data:
        word = word.strip()

        if catDogRegex.search(word):
            values['contain cat or dog'] += 1
        if fourLetterRegex.search(word):
            values['contain four letters'] += 1
        if hunRegex.search(word):
            values['contain \'hun\''] += 1
        if INGRegex.search(word):
            values['end with \'ing\''] += 1
        if IONRegex.search(word):
            values['end with \'ion\''] += 1
        if notQURegex.search(word):
            values['contain a \'q\' not immediately followed by a \'u\''] += 1
        if noVowelRegex.search(word):
            values['contain no vowels'] += 1
        if onlyVowelsRegex.search(word):
            values['contain only vowels'] += 1
        if endingwithNOTRegex.search(word):
            values['end with \"\'nt\"'] += 1
        if twoVowelsrowRegex.search(word):
            values['contain two vowels in a row'] += 1
        if twoVowelsRegex.search(word):
            values['contain at least two vowels'] += 1

    print("\n")
    for value in values:
        print("There are",str(values[value]),"words that",value+".")
    # print(values)


"""
def test(words):
    count = 0
    testRegex = re.compile(r'\'+:*;*')
    for word in words:
        if testRegex.search(word):
            count+=1
            # print(word)
    print(count)"""

def moreRegex():
    print("""The .* will match everything except a newline however it differs with .*? in such that .*? is the non-greedy
version of .*. This simply means for .*? if anything comes up that matches with the pattern immediately it will
end matching whereas for .* it will try to keep on matching till the pattern ends and in this case till a new line.""")
    print("\n")
    matchingNames()
    print("\n")
    matchNuminWords()
    print("\n")
    dolVals()
    print("\n")

def matchingNames():
    names = ['Satoshi Nakamoto','Alice Nakamoto','Robocop Nakamoto','satoshi Nakamoto','Mr. Nakamoto','Nakamoto','Satoshi nakamoto']

    namesRegex = re.compile(r'^([A-Z][A-z]*)\s+(Nakamoto)$')
    for name in names:
        if namesRegex.search(name):
            print (name + ":", True)
        else:
            print(name + ":", False)

def matchNuminWords():
    testNums = ['twenty','twenty-four','thirty','thirty five','sixty-six','eighty-three','ninety-nine','forty se','ninety-ten','thirsty-two']

    matchNumRegex = re.compile(r'^(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)-?(one|two|three|four|five|six|seven|eight|nine)?$')

    for num  in testNums:
        if matchNumRegex.search(num):
            print(num, True)
        else:
            print(num, False)

def dolVals():
    testVals = ['$100.00','$10,000.00','$1234','$5000.00','$1,000,000','$1234.567','$50,00.00','$1234,567','$1,234.567','1234','#1234']
    dolValsRegex = re.compile(r'^(\$)(\d*|\d{1,3}(,\d{3})*)(.\d{2})?$')

    for val in testVals:
        if dolValsRegex.search(val):
            print(val, True)
        else:
            print(val, False)

def strongPass():
    testPass = ['dnttnMwM*486','dnttMM*486','iasP123','Modula-2','testpass99','testpass','test69Pass','testPass23','Testpass234','teStpass239','teStPasS90','strongPass']
    strongPassRegex = re.compile(r'^(?=.{8,})(?=.*[A-Z])(?=.*[a-z])(?=.*\d).+')

    for password in testPass:
        if strongPassRegex.search(password):
            print(password,'is a strong password')
        else:
            print(password,'is a weak password')

def strongerPass():
    import random

    password = ""
    strongerPassRegex = re.compile(r'^[a-z]{4,}$')
    words = []
    data = open('words.txt', 'r')
    for line in data:
        line = line.strip()
        if strongerPassRegex.search(line):
            words.append(line)

    for _ in range(4):
        word = random.choice(words)
        password += word
        # print(word)
        words.remove(word)

    print(password)


def main():
    regexDictionary()
    print("\n")
    moreRegex()
    print("\n")
    strongPass()
    print("\n")
    for _ in range(5):
        strongerPass()
main()