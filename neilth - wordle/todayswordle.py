#This code automaticly solves todays wordle
#When it asks for input leave blank if you just want todays wordle
#you solve any worlde from wordle #1 to wordle #2309



while True: 
    from data2 import answers
    from datetime import date
    from datetime import datetime
    today = date.today()
    diff = ((datetime.strptime(today.strftime("%d/%m/%Y"), "%d/%m/%Y")).date() - (datetime.strptime('19/6/2021', "%d/%m/%Y")).date()).days 

    wordledate = input("Which wordle? (Today is Wordle #"+str(diff)+")")
    if wordledate != "":
        diff = int(wordledate)

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


    avg = []
    y = 0
    while factual:
        import json
        y+=1
        fullimage = []
        answer = answers[diff-1]
        #print(answer)
        unsolved = True
        guess = random.choice(possiblewords)
        contain = ["","","","",""]
        none = []
        has = [[],[]]
        
        my_list = []
        possible = possiblewords
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

            
            x+=1
            
            ploop = {}
            for word in possible:
                ploop[word] = freq[word]
            
            if len(possible) < 2:
                #print("🟩🟩🟩🟩🟩"+" "+possible[0])
                fullimage.append("🟩🟩🟩🟩🟩"+" "+possible[0])
                #print("Correct answer: "+answer)
                #print("Guessed: "+guess)
                #print(str(len(possible))+" possibilities")
                #print("Known pattern"+str(contain))
                #print("Doesn't include" +str(none))
                #print("has; but not @: "+str(has))
                #print("Took "+str(x)+" tries")
                #avg.append(x)
                #print(sum(avg))
                #print("avg: "+str(sum(avg)/len(avg)))
        
                
                #print(guess)
                
                unsolved = False
                #print(possible)
            else:
                #print("".join(image)+" "+guess)
                fullimage.append("".join(image)+" "+guess)
        
                guess = max(ploop, key=ploop.get)
        
        #print("Game #"+str(y))
        
        if x == 2 or x == 3:
            break

    print("Wordle "+str(diff)+" "+str(x)+"/6"+"\n")
    for line in fullimage:
        print(line)
    print("\n\n\n")