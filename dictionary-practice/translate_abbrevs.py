## Exercise 3: Translate abbreviations

# You are the parent of 3 teenage children, and you have no idea what they are saying in their texts. You decided to write a program to translate the abbreviations they use in their texts to plain english. You will write a program that prompts the user to enter a text message, translate the text message to plain english, and print out the results.

# Example usage:
# ```
# $ python txt_xlator.py
# What is the text?
# > jk lol
# Just kidding Laughing out loud
# ```

# You have access to a dictionary of abbreviations. Use the built-in json module to read in the abbv.json file. Like so:

import json
file = open('abbv.json', 'r')
abbreviations = json.loads(file.read())
# print abbreviations

text_message = raw_input("Enter a text message: ").upper()
words = text_message.split(' ')
print words

for word in words:
    if word in abbreviations:
        print abbreviations[word]
    else:
        print word.lower()

file.close()
