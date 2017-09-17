import argparse


class JugglerPassGen(object):
    mapping = {'a': 'a@4A', 'b': 'bB8', 'c': 'cC', 'd': 'dD', 'e': 'e3€&E', 'f': 'fF', 'g': 'gG', 'h': 'hH',
               'i': 'i1!I', 'l': 'l|£L', 'm': 'mM', 'n': 'nN', 'p': 'pP', 'q': 'qQ', 'r': 'rR', 's': 's5$S',
               't': 't7T', 'u': 'uU', 'v': 'vV', 'z': 'zZ', 'o': 'o0O'}
    divisor = {'.', '-', '_'}

    def __init__(self, word):
        self.word = word

    @staticmethod
    def dictionary(input_character):
        """
        return an iterable based on dictionary and input_character
        """
        return JugglerPassGen.mapping.get(input_character, input_character)

    @staticmethod
    def generate(base):
        """
        Generate all possible combination with charters and their substitution of a word
        """
        if base == '':
            yield base
        else:
            for character in JugglerPassGen.dictionary(base[0]):
                for rest in JugglerPassGen.generate(base[1:]):
                    yield character + rest

    def password_generator(self):
        """
        Generate all possible password from a word using JugglerPassGen.generate method
        """
        password_list = []
        for generated in JugglerPassGen.generate(self.word):  # call the function for permutations
            password_list.append(generated)
        return password_list

    def years(self):
        """
        Add years to results of JugglerPassGen.password_generator
        """
        password_list = []
        year_start = int(input("Years range start at: "))
        year_stop = int(input("Years range stop at: "))
        for generated in JugglerPassGen.generate(self.word):
            for year in range(year_start, year_stop + 1):
                modified_record = generated + str(year)
                password_list.append(modified_record)
                year = year % 100
                modified_record = generated + str('%02d' % year)
                password_list.append(modified_record)
        return password_list

    def years_with_separator(self):
        """
        Add years to results of JugglerPassGen.password_generator and insert a separator between year and word
        """
        password_list = []
        year_start = int(input("Years range start at: "))
        year_stop = int(input("Years range stop at: "))
        for generated in JugglerPassGen.generate(self.word):
            for year in range(year_start, year_stop + 1):
                modified_record = generated + str(year)
                password_list.append(modified_record)
                for div in JugglerPassGen.divisor:
                    modified_record = generated + div + str(year)
                    password_list.append(modified_record)
                year = year % 100
                modified_record = generated + str('%02d' % year)
                password_list.append(modified_record)
                for div in JugglerPassGen.divisor:
                    modified_record = generated + div + str('%02d' % year)
                    password_list.append(modified_record)
        return password_list


# SCRIPT MAIN SECTION
title = """
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
 
"""
print(title)
parser = argparse.ArgumentParser()
parser.add_argument("words", nargs=1, help="Comma separated words")
parser.add_argument("filename", nargs=1, help="Name of the output file")
parser.add_argument("-p", "--password", action="store_true", help="Do only character substitution")
parser.add_argument("-y", "--years", action="store_true", help="Do character substitution and year append")
parser.add_argument("-s", "--separator", action="store_true", help="""Do character substitution, years append and insert
                                                                  a separator between years and words""")
args = parser.parse_args()
filename = str(args.filename[0])
output_filename = open(filename, "a")  # The ,"a" will append the output to the file
list_of_words = args.words[0].split(",")
generated_password = []

if args.password:
    for single_word in list_of_words:
        print(list_of_words)
        instanced_class = JugglerPassGen(single_word)
        generated_password.extend(instanced_class.password_generator())
    for record in generated_password:
        record = record + "\n"
        output_filename.write(record)
if args.years:
    for single_word in list_of_words:
        years_instanced_class = JugglerPassGen(single_word)
        generated_password.extend(years_instanced_class.years())
    for record in generated_password:
        record = record + "\n"
        output_filename.write(record)
if args.separator:
    for single_word in list_of_words:
        years_with_separator_instanced_class = JugglerPassGen(single_word)
        generated_password.extend(years_with_separator_instanced_class.years_with_separator())
    for record in generated_password:
        record = record + "\n"
        output_filename.write(record)
elif args.password == args.years == args.separator == False:
    print("Select an option, use -h for help")

output_filename.close()
exit()
