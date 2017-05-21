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
    for generated in generate(base):
        generated = generated + "\n"
        outfilename.write(generated)
########### SCRIPT MAIN SECTION ##########
Input_Name = input("Type a word ")
filename = input("Type an output file name ")
outfilename = open(filename,"w")
passgen(Input_Name)
outfilename.close()
