def dictionary(input_character):
    mapping={'a':'a@4A', 'b':'bB8', 'c':'cC', 'd':'dD','e':'e3€&E', 'f':'fF', 'g':'gG', 'h':'hH', 'i':'i1!I', 'l':'l|£L', 'm':'mM', 'n':'nN', 'p':'pP', 'q':'qQ', 'r':'rR', 's':'s5$S', 't':'t7T', 'u':'uU', 'v':'vV', 'z':'zZ', 'o':'o0O'}
    return mapping.get(input_character,input_character)

def generate(base):
    if base=='': yield base
    else:
        for character in dictionary(base[0]):
            for rest in generate(base[1:]):
                yield character+rest

def passgen(base):
    passlist=[]
    for generated in generate(base):
        generated = generated + "\n"
        passlist.append(generated)
    for record in passlist:
        outfilename.write(record)

def years(base):
    passlist=[]
    year_start = int(input("Years range start at: "))
    year_stop = int(input("Years range stop at: "))
    for generated in generate(base):
        for year in range(year_start,year_stop+1):
            modified_record = generated+str(year)
            passlist.append(modified_record)
            year = year % 100
            modified_record = generated+str('%02d'%year)
            passlist.append(modified_record)
    for record in passlist:
        record = record + "\n"
        outfilename.write(record)

def pointedyears(base):
    passlist=[]
    year_start = int(input("Years range start at: "))
    year_stop = int(input("Years range stop at: "))
    divisor =['.','-','_']
    for generated in generate(base):
        for year in range(year_start,year_stop+1):
            modified_record = generated+str(year)
            passlist.append(modified_record)
            for div in divisor:
                modified_record = generated+div+str(year)
                passlist.append(modified_record)
            year = year % 100
            modified_record = generated+str('%02d'%year)
            passlist.append(modified_record)
            for div in divisor:
                modified_record = generated+div+str('%02d'%year)
                passlist.append(modified_record)
    for record in passlist:
        record = record + "\n"
        outfilename.write(record)
        
options = {'s':passgen,'y':years,'p':pointedyears,'S':'symbols','A':'all'}     
def main():
    select = str(input("Select a modifier: \ns for substitution\ny for years append\np for pointed years append\n"))
    return select        

########### SCRIPT MAIN SECTION ##########
title ="""
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
\nthis script modify words to generate valid password with some common pattern:\n\n\n
Subtitution: Do a substitution of every character in the word with a similar number or symbols, this option also do lowercase to uppercase modification and vice versa
Year: Same as substitution with the add of a year ate the end of the word. User can specify the years range. 
"""
print (title)
Input_Name = input("Type a word ")
filename = input("Type an output file name ")
User_choice = main()
outfilename = open(filename,"a")
options[User_choice](Input_Name)
outfilename.close()
