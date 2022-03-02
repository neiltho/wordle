#baiscly runs wordle and wordle solver in the same code to get results fast
#word is a random word from the list given by wordle
#first guess is a random word too

import random
from time import sleep
factual = True
from data2 import freq
from data2 import possiblewords
#from data2 import freq

#filter that filters a letter out of a list
def filter(word,list):
    x = True
    for letter in list:
        if letter in word:
            x = False
    return x

#filter used for contain or the green tiles, it removes 
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
wordlist = possiblewords

avg = []
y = 0
while factual:
    import json
    y+=1
    
    answer = random.choice(wordlist)
    unsolved = True
    guess = random.choice([x for x in wordlist for letter in x if len(set(x)) == 5 and "x" not in x and "z" not in x])
    contain = ["","","","",""]
    none = []
    has = [[],[]]
    my_list = []
    possible = wordlist
    x = 0
    ploop = {}
    image = ["","","","",""]
    print("\n")
    print("\n")
    
    while unsolved:
        
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                contain[i] = guess[i]
                image[i] = "🟩"
            if guess[i] != answer[i] and guess[i] in answer:
                has[0].append(guess[i])
                has[1].append(i)
                image[i] = "🟨"
            if guess[i] not in answer:
                none.append(guess[i])
                image[i] = "⬛"
            
                
        none = list(set(none))
        
        if len(has[0]) != 0:
            possible = [x for x in possible if filter(x,none) == True and filter(x,has[0]) == False and filter2(x) == True and filter3(x) == True]
        else:
            possible = [x for x in possible if filter(x,none) == True and filter2(x) == True]
        
        
        #possible.sort()
        
        x+=1
        
        ploop = {}
        for word in possible:
            ploop[word] = freq[word]
        
        if len(possible) < 2:
            print("🟩🟩🟩🟩🟩"+" "+possible[0])
            #print("Correct answer: "+answer)
            #print("Guessed: "+guess)
            #print(str(len(possible))+" possibilities")
            print("Known pattern"+str(contain))
            print("Doesn't include" +str(none))
            print("has; but not @: "+str(has))
            print("Took "+str(x)+" tries")
            avg.append(x)
            print(sum(avg))
            print("avg: "+str(sum(avg)/len(avg)))
    
            
            unsolved = False
            print(possible)
        else:
            print("".join(image)+" "+guess)
        
    
            guess = max(ploop, key=ploop.get)
    
    print("Game #"+str(y))
    sleep(0)
#Avrage of 3.95 tries