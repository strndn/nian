#Lukas Strand 020202-7157
def getWords():
    text_file = open('svenskaOrd.txt', 'r')
    words_list = text_file.read().split('\n')
    return words_list

def getInput():
    while True:
        puzzleLetters = input("Nian: ")
        if len(puzzleLetters) == 9:
            return puzzleLetters
        print('Antal tecken skall vara 9 stycken!')

def checkForWords(letters, words_list):
    temp_list = []
    temp_list2 = []
    wantedWords_list = []

    letter_list = list(letters)
    allowed_chars = set(letters)
    amountOfChar_list = []


    for letter in letter_list:
        amountOfChar_list.append(letters.count(letter))

    for word in words_list:
        if  letter_list[4] in word and len(word)>= 4:
            temp_list.append(word)
    
    for word in temp_list:
        if set(word).issubset(allowed_chars):
            temp_list2.append(word)
    
    for word in temp_list2:
        i = 0
        exits = False
        for letter in letter_list:
            if word.count(letter) <= amountOfChar_list[i]:
                i+=1
                exits = True
            else:
                exits = False
                break
        if exits == True:
            wantedWords_list.append(word)

    return wantedWords_list

wantedWords = checkForWords(getInput(), getWords())
wantedWordsUsingAllLetters = []

for word in wantedWords:
    print(word)
    if len(word) == 9:
        wantedWordsUsingAllLetters.append(word)
print()
print(len(wantedWordsUsingAllLetters),'ord använder alla bokstäver:')
for word in wantedWordsUsingAllLetters:
    print(word)

