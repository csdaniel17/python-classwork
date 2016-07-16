## Navigating nested dictionaries

# Given this "user" dictionary which stores information about a user:

aditi = {
  'name': 'Aditi',
  'email': 'aditi@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# 1. Write a python expression that gets the email address of Aditi.
print aditi['email']

# 2. Write a python expression that gets the first of Aditi's interests.
print aditi['interests'][0]

# 3. Write a python expression that gets the email address of Jasmine.
print aditi['friends'][0]['email']
# option 2:
# print aditi['friends'][0].get('email')

# 4. Write a python expression that gets the second of Jan's two interests.
print aditi['friends'][1]['interests'][1]
