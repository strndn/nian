#Lukas Strand 020202-7157

#Hämtar ord från text filen.
def getWords():
    text_file = open('svenskaOrd.txt', 'r')
    words_list = text_file.read().split('\n')
    return words_list

#Tar in input.
def getInput():
    while True:
        letters = input("Nian: ").lower()
        if len(letters) == 9 and letters.isalpha():
            return letters
        print('Antal tecken skall vara 9 stycken och det får endast vara bokstäver!')

#Gör en lista som innehåller antalet för varje bokstav.
def getCharAmountL(letter_list, letters):
    amountOfChar_list = []
    for letter in letter_list:
        amountOfChar_list.append(letters.count(letter))
    return amountOfChar_list

#Gör en lista med ord som innehåller mittersta bokstaven.
def getListContMidChar(letter_list, words_list):
    tempWord_list = []
    for word in words_list:
        if  letter_list[4] in word and len(word)>= 4:
            tempWord_list.append(word)
    return tempWord_list

#Gör en lista som endast innehåller de inmatade bokstäverna.
def getListContWords(tempWord_list, allowedChars):
    contWord_list = []
    for word in tempWord_list:
        if set(word).issubset(allowedChars):
            contWord_list.append(word)
    return contWord_list

#Gör den slutgiltiga listan med de ord som kan hittas i pusslet.
#Genom att jämnföra alla ord som innehåller de tillåtna bokstäverna
#mot listan som innehåller hur många av dessa bokstäver som ordet får innehålla.
def getWantedWords(contWord_list, letter_list, amountOfChar_list):
    wantedWords_list = []
    for word in contWord_list:
        i = 0
        isOkay = False
        for letter in letter_list:
            if word.count(letter) <= amountOfChar_list[i]:
                i+=1
                isOkay = True
            else:
                isOkay = False
                break
        if isOkay == True:
            wantedWords_list.append(word)
    return wantedWords_list

#Kontrollerar och returnerar en lista med det eftertraktade orden.
def checkForWords(letters, words_list):
    letter_list = list(letters)
    allowedChars = set(letters)
    return getWantedWords(getListContWords(getListContMidChar(letter_list, words_list), allowedChars), letter_list, getCharAmountL(letter_list, letters))

#Startar programmet
wantedWords = checkForWords(getInput(), getWords())
wantedWordsUsingAllLetters = []

#Skriver ut orden.
for word in wantedWords:
    print(word)
    if len(word) == 9:
        wantedWordsUsingAllLetters.append(word)
print()
print(len(wantedWordsUsingAllLetters),'ord använder alla bokstäver:')
for word in wantedWordsUsingAllLetters:
    print(word)