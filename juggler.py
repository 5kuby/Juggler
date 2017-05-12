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
    generatedpasslist = []  #initializing the list of generated password
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
        generatedpasslist.append(generatedpass) #add the generated pass to the output list
    return generatedpasslist #return the list of generated password
Input_Name = input("Type a word ")
filename = input("Type an output file name ")
outfilename = open(filename,"w")
namepassword = sub_a(Input_Name)
for entry_a in namepassword:
    entry_a = entry_a + "\n"
    outfilename.write(entry_a)
outfilename.close()
