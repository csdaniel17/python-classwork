## Bonus: Exercise 4 - Cracking Passwords

# You hacked into a high-security system and found a database of user accounts. The only problem is the passwords have been encrypted. You know that md5 is a popular but weak hashing scheme that is used by many companies to encrypt user passwords. If you are lucky, you can use a rainbow table attack using common english words from a dictionary to recover the plain-text passwords.

# You have access to a list of the most common words common_words.txt, and the user accounts: accounts.json. Read up on how to use md5:

# https://docs.python.org/2/library/md5.html

# Here's an example of how someone might use md5 to generate an encrypted password:

import md5
import json

text = open('common_words.txt')
content = text.read()

# read into json file
file = open('accounts.json', 'r')
accounts = json.loads(file.read())

words = content.split('\n')
encrypted_common_words = {}

for word in words:
    plaintext_password = word
    m = md5.new()
    m.update(plaintext_password)
    encrypted_password = m.hexdigest()
    encrypted_common_words[encrypted_password] = word

for account in accounts:
    password = account.get('password')
    username = account.get('username')
    if password in encrypted_common_words:
        print username + ': ' + encrypted_common_words[password]
    else:
        print username + ": i couldn't crack your password!"

text.close()
file.close()
## to check:
# plaintext_password = 'raven'
# print plaintext_password
# m = md5.new()
# m.update(plaintext_password)
# encrypted_password = m.hexdigest()
# print encrypted_password
## checks out. yay!
