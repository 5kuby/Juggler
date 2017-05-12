"""


  ___                   _           
  |_  |                 | |          
    | |_   _  __ _  __ _| | ___ _ __ 
    | | | | |/ _` |/ _` | |/ _ \ '__|
/\__/ / |_| | (_| | (_| | |  __/ |   
\____/ \__,_|\__, |\__, |_|\___|_|   
              __/ | __/ |            
             |___/ |___/             

                            By
                     _____ _          _           
                    |  ___| |        | |          
                    |___ \| | ___   _| |__  _   _ 
                        \ \ |/ / | | | '_ \| | | |
                    /\__/ /   <| |_| | |_) | |_| |
                    \____/|_|\_\\__,_|_.__/ \__, |
                                            __/ |
                                            |___/ 
this script modify words to generate valid password with some common pattern

"""
from itertools import product
from random import randint
def sub_a(word):    #Defining the function that substitute the 'a' char with some alternatives
    x = 'a'
    y = '@'
    z = '4'
    m = 'A'
    var_list = [x,y,z,m]    #putting all alternatives ina a list
    outlist_a = []
    n_match = word.count('a')   #count how many 'a' characters there are in the word
    for count in product(var_list,repeat=n_match):  #this instruction generate a tuple with all possible combination of n symbols, n is the occourrence of 'a' in the word
        listed_count = list(count)  #this instruction and the below one convert the tuple in a list
        outlist_a.append(listed_count) 
    list_leng=len(outlist_a)
    generatedpasslist_A = []  #initializing the list of generated password
    for comb in outlist_a: #do a substitution for every combination of symbols
        counter=0 #this is needed for the cycle below and must be resetted for every combination
        generatedpass='' #this is the variable used to store the generated password, it will be append to the list "generatedpasslist"
        for letter in word: #do a ceck for every letter in word
            if letter != 'a': #if the letter aren't 'a' it must be unchanged in generatedpass variable becaus this function must change only the 'a' character
                generatedpass = generatedpass + letter
            if letter == 'a': #if letter is 'a' the change must be done
                letterx = comb[counter] #counter will be increased for every 'a' match in the word. Comb is a nestled list. The condition of this if will be matched for every 'a' in the word, increasing the counter var with the instruction below the next 'a' match will use a different symbol of the previosu one
                generatedpass = generatedpass + letterx #this instrucion change the original letter with the symbol
                counter = counter+1 #read above
        generatedpasslist_A.append(generatedpass) #add the generated pass to the output list
    return generatedpasslist_A #return the list of generated password
def sub_e(word):    #Defining the function that substitute the 'e' char with some alternatives
    x = 'e'
    y = '3'
    z = '€'
    m = 'E'
    var_list = [x,y,z,m]    
    outlist_e = []
    n_match = word.count('e')   
    for count in product(var_list,repeat=n_match):  
        listed_count = list(count)  
        outlist_e.append(listed_count) 
    list_leng=len(outlist_e)
    generatedpasslist_E = [] 
    for comb in outlist_e: 
        counter=0 
        generatedpass='' 
        for letter in word: 
            if letter != 'e': 
                generatedpass = generatedpass + letter
            if letter == 'e': 
                letterx = comb[counter] 
                generatedpass = generatedpass + letterx 
                counter = counter+1 
        generatedpasslist_E.append(generatedpass) 
    return generatedpasslist_E
def sub_t(word):    #Defining the function that substitute the 't' char with some alternatives
    x = 't'
    y = '7'
    z = 'T'
    var_list = [x,y,z]    
    outlist_t = []
    n_match = word.count('t')   
    for count in product(var_list,repeat=n_match):  
        listed_count = list(count)  
        outlist_t.append(listed_count) 
    list_leng=len(outlist_t)
    generatedpasslist_T = [] 
    for comb in outlist_t: 
        counter=0 
        generatedpass='' 
        for letter in word: 
            if letter != 't': 
                generatedpass = generatedpass + letter
            if letter == 't': 
                letterx = comb[counter] 
                generatedpass = generatedpass + letterx 
                counter = counter+1 
        generatedpasslist_T.append(generatedpass) 
    return generatedpasslist_T
def sub_o(word):    #Defining the function that substitute the 'o' char with some alternatives
    x = 'o'
    y = '0'
    z = 'O'
    var_list = [x,y,z]    
    outlist_o = []
    n_match = word.count('o')   
    for count in product(var_list,repeat=n_match):  
        listed_count = list(count)  
        outlist_o.append(listed_count) 
    list_leng=len(outlist_o)
    generatedpasslist_O = [] 
    for comb in outlist_o: 
        counter=0 
        generatedpass='' 
        for letter in word: 
            if letter != 'o': 
                generatedpass = generatedpass + letter
            if letter == 'o': 
                letterx = comb[counter] 
                generatedpass = generatedpass + letterx 
                counter = counter+1 
        generatedpasslist_O.append(generatedpass) 
    return generatedpasslist_O
########### SCRIPT MAIN SECTION ##########
Input_Name = input("Type a word ")
filename = input("Type an output file name ")
outfilename = open(filename,"w")
namepassword_A = sub_a(Input_Name)
namepassword_E = sub_e(Input_Name)
namepassword_T = sub_t(Input_Name)
namepassword_O = sub_o(Input_Name)
for entry_a in namepassword_A:
    entry_a = entry_a + "\n"
    outfilename.write(entry_a)
for entry_e in namepassword_E:
    entry_e = entry_e + "\n"
    outfilename.write(entry_e)
for entry_t in namepassword_T:
    entry_t = entry_t + "\n"
    outfilename.write(entry_t)
for entry_o in namepassword_O:
    entry_o = entry_o + "\n"
    outfilename.write(entry_o)
outfilename.close()
