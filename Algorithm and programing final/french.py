'''lexicon_file = 'AlgorithmProgramming_FinalProject-main/Algorithm and programing final/assets/muaha the french.txt'

with open(lexicon_file, 'r') as f:
    words = [line.strip() for line in f]

print(words[:])'''

#f = open("Algorithm and programing final/assets/muaha the french.txt", "r")


with open('Algorithm and programing final/assets/lang_french.txt', 'r') as f:
    french_words_lst = [line.strip() for line in f]
french_words_lst.sort(key=len)

french_len_indexes = []
french_length = 1


for i in range(len(french_words_lst)): #to generate the index of len_indexes, i made a for loop where if the lenth of a word in wordlist is bigger than 'length', then it does the following:
    if len(french_words_lst[i]) > french_length: #it starts with the lenth of 2
        french_length +=1
        french_len_indexes.append(i)

french_len_indexes.append(len(french_words_lst))


print (french_words_lst[52])


x = 1
def insane():
    y = x


with open("words.txt", "r") as file:
    wordlist = [line.strip() for line in file.readlines()]