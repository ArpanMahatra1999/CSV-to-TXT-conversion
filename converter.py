import pandas as pd

emotions_csv = pd.read_csv('emotions.csv')
emotions_txt = open('emotions.txt', 'w')

for i in range(len(emotions_csv)):
    string_of_important_chars = ""
    for character in emotions_csv['synonyms'][i]:
        if character == "[" or character == "]" or character == " " or character == "\'":
            pass
        else:
            string_of_important_chars = string_of_important_chars + character
    array_of_synonyms = (string_of_important_chars.split(","))
    for synonym in array_of_synonyms:
        emotions_txt.write(" '" + synonym + "': '" + emotions_csv['name'][i] + "',\n")