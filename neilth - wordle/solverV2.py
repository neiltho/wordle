
import random
from time import sleep
from unicodedata import east_asian_width
#from data2 import freq

def filter(word,list):
    x = True
    for letter in list:
        if letter in word:
            x = False
    return x

def filter2(word):
    x = True
    for i in range(len(contain)):
        if contain[i] != "":
            if contain[i] != word[i]:
                x = False
    return x
            
def filter3(word):
    x = True
    for i in range(len(has[0])):
        if has[0][i] == word[has[1][i]]:
            x = False
    return x


print("welcome to wordle solver")
wordlist = []
with open("wordle-allowed-guesses.txt") as file:
        for line in file:
            wordlist.append(line.rstrip())
            
avg = []
while True:
    answer = random.choice(wordlist)
    unsolved = True
    guess = random.choice(wordlist)
    contain = ["","","","",""]
    none = []
    has = [[],[]]
    my_list = []
    possible = wordlist
    x = 0

    while unsolved:
        
        
        
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                contain[i] = guess[i]
            if guess[i] != answer[i] and guess[i] in answer:
                has[0].append(guess[i])
                has[1].append(i)
            if guess[i] not in answer:
                none.append(guess[i])
                
        none = list(set(none))
        
        if len(has[0]) != 0:
            possible = [x for x in possible if filter(x,none) == True and filter(x,has[0]) == False and filter2(x) == True and filter3(x) == True]
        else:
            possible = [x for x in possible if filter(x,none) == True and filter2(x) == True]
        
        
        possible.sort()
        
        x+=1

    
        
        guess = possible[0]
        
        if len(possible) < 2:
            print("\n")
            print("Correct answer: "+answer)
            print("Guessed: "+guess)
            print(str(len(possible))+" possibilities")
            print("Known pattern"+str(contain))
            print("Doesn't include" +str(none))
            print("has; but not @: "+str(has))
        
            unsolved = False
            print("Took "+str(x)+" tries")
            avg.append(x)
            print("avg: "+str(sum(avg)/len(avg)))
            print(possible)
    sleep(0.5)