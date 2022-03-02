#This is wordle made with python very simple base code for solver2.py and solver3.py



import time
import random
from data2 import possiblewords
wordlist = possiblewords
unsolved = True
guesses = 0
image = []
word = random.choice(wordlist)
#print(word)

print("WORDLE CLONE! enter a word(5 LETTER ONLY)")
while unsolved:
    guess = ""
    guesses += 1
    pattern = ""
    while len(guess) != 5:
        guess = input("")
    
    if word == guess:
        unsolved = False
    for i in range(len(guess)):
        if guess[i] == word[i]:
            pattern += "🟩"
        if guess[i] != word[i] and guess[i] in word:
            pattern += "🟨"
        if guess[i] not in word:
            pattern += "⬛"
    image.append(pattern+" "+guess)
    if guesses == 6:
        unsolved = False
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
    for line in image:
        print(line)
if guess == word:
    print("CORRECT")
else:
    print("correct word was "+word.upper())