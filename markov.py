#!/usr/bin/env python
from sys import argv

script, filename = argv

print "Youre in the right file."

f = open(filename)
pre_text = f.read()

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""


    new_text = pre_text.lower()

    newer_text = new_text.replace("!", " ")
    text_1 = newer_text.replace("?", " ")
    text_2 = text_1.replace(".", " ")
    text_3 = text_2.replace(":", " ")
    text_4 = text_3.replace(";", " ")
    text_5 = text_4.replace("'", "")
    text_6 = text_5.replace("-", " ")
    text_7 = text_6.replace(",", " ")
    text_8 = text_7.replace("\n", " ")
    text_final = text_8.replace("  ", " ")
    print text_final# make a list of words
    split_text = text_final.split(" ")
    print split_text

    # 
    list1 = []
    list2 = []


    for word in split_text:
        list1.append(word)

    for word in split_text[1: -1]:
        list2.append(word)

    toop_list = zip(list1, list2)

    # print "Here is list1:"
    # print list1

    # print "Here is list2:"
    # print list2

    print "Here's the toop"
    print toop_list

    full_text = split_text[2:]
# populate the dictionary with the toop_list as keys
    dict_toop = {}
   # dict_toop = {toop_list[0], split_text[2]}
   # print dict_toop
    for x in range(len(toop_list)):
        print x
        if toop_list[x] in dict_toop:
            #dict_toop[toop_list[x]].append(full_text[x])
            pass          
        else:
            dict_toop[toop_list[x]] = full_text[x]

        
    print dict_toop


  #  print dict_toop
# chain_dict[first two words] = third word
# chain_dict[second and third word] = fourth word
#     #     
#     return {}

# def make_text(chains):
#     """Takes a dictionary of markov chains and returns random text
#     based off an original text."""
#     return "Here's some random text."

# def main():
#     args = sys.argv

#     # Change this to read input_text from a file
#     input_text = "Some text"

#     chain_dict = make_chains(input_text)
#     random_text = make_text(chain_dict)
#     print random_text

# if __name__ == "__main__":
#     main()
make_chains(pre_text)