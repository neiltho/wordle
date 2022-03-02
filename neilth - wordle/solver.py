from data2 import possiblewords


#This code is very ineffecent and doesn't work anymore. You need to manullay play wordle and input the pattern that u recive after typing a certain word. Also it wouldnt filter out certain words




def combine(string1,string2):
    x = True
    for letter in list(string1.strip()):
        if letter not in string2:
            x = False
    if x == False:
        return string2
    
    
    final = ""
    if string2.strip() == "":
        return string1
    if string1 == string2:
        return string1
    for i in range (len(string1)):
        if string1[i] != " ":
            final += string1[i]
        if string2[i] != " ":
            final += string2[i]
        else:
            final += " "
    return final

print("welcome to the wordle solver! ")
print("keep in mind that the best word to start with is CRANE ")

unsolved = True
possible = possiblewords
contain = ""
reduce = []
none = []
new = "     "
contain = ""
guess = ""
pattern = ""
has = []
hasloc = []
ploop = []


while unsolved:
    contain = ""
    guess = ""
    pattern = ""
    has = []
    hasloc = []
    cnt = {}

    while len(guess) != 5:
        guess = (str(input("guessed word? (5 letters)"))).lower()

    while len(pattern) != 5:
        pattern = (str(input(" What is the pattern of the word? (in g y n)"))).lower()

    for i in range(len(guess)):
        if pattern[i] == "g":
            contain += guess[i]
        if pattern[i] == "y":
            has.append(guess[i])
            hasloc.append(i)
            contain += " "
        if pattern[i] == "n": 
            contain += " "
            if guess[i] not in contain:
                none.append(guess[i])
            else:
                has.append(guess[i])
                hasloc.append(i)
    none = list(set(none))

            
    
    contain = combine(contain,new)

    for string in possible:
        you = True
        for i in range(len(string)):
            if contain[i] == " ":
                pass
            else:
                if contain[i] != string[i]:
                    you = False
                
        if you == True:
            reduce.append(string)
            reduce = list(set(reduce))
            
    my_list = []
    if len(has) != 0:
        if len(has) == 1:
            for word in reduce:
                if has[0] in word:
                    my_list.append(word)
        if len(has) == 2:
            for word in reduce:
                if has[0] in word and has[1] in word:
                    my_list.append(word)
        if len(has) == 3:
            for word in reduce:
                if has[0] in word and has[1] in word and has[2] in word:
                    my_list.append(word)
        if len(has) == 4:
            for word in reduce:
                if has[0] in word and has[1] in word and has[2] in word and has[3] in word:
                    my_list.append(word)
        if len(has) == 5:
            for word in reduce:
                if has[0] in word and has[1] in word and has[2] in word and has[3] in word and has[4] in word:
                    my_list.append(word)
        reduce = my_list

    my_list = []
    if len(has) != 0:
        for word in reduce:
            l = False
            for i in range(len(has)):
                if word[hasloc[i]] == has[i] :
                    l = True
            if l == True:
                pass
            else:
                my_list.append(word)
        reduce = my_list



    #if len(none) != 0:
       # for word in reduce:
         #       for letter in none:
          #          if letter in word:
          #              reduce.remove(word)
                        

    
    for word in reduce:
        for i in range(len(guess)):
            if word[i] != contain[i]:
                if word in reduce:
                    reduce.remove(word)
    reduce.sort()
    
    
    
    
    
    if len(reduce) != 0:
        for word in reduce:
            for letter in set(word):
                cnt[letter] = 0
        for word in reduce:
            for letter in set(word):
                cnt[letter] += 1
        
        
        max_key = max(cnt, key=cnt.get)
        for letter in none:
            if letter in cnt:
                cnt.pop(letter)
        for letter in list(contain):
            if letter in cnt:
                cnt.pop(letter)
        for letter in has:
            if letter in cnt:
                cnt.pop(letter)
        max_key = max(cnt, key=cnt.get)
        for word in reduce:
            if max_key in word:
                ploop.append(word)
        cnt.pop(max_key)
        max_key = max(cnt, key=cnt.get)
        for word in ploop:
            if max_key not in ploop:
                ploop.remove(word)
        cnt.pop(max_key)
        max_key = max(cnt, key=cnt.get)
        for word in ploop:
            if max_key not in ploop:
                ploop.remove(word)
    
    
    reduce.sort()
        
    print("The word has")
    print(list(contain))
    print("The word contains the letters")
    print(has)
    print(hasloc)
    print("The word doesn't contain")
    print(none)
    print("There are "+str(len(reduce))+" possibilities.")
    print(reduce)
    
    
    print(cnt)
    print(ploop)
    if len(ploop) != 0:
        print("Try guessing: "+ploop[0])
    else:
        print("Try guessing: "+reduce[0])
    
    
    possible = reduce
    new = contain
    
    if len(reduce) < 2:
        unsolved = False
    
print("wordle solved!")