favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title())

jin_pin = {
    'first_name': 'jinpin',
    'last_name': 'z',
    'age': 41,
    'city': 'hb',
}
print(jin_pin)


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# travel the sorted output
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# travel the dictionary values
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# use set to fix repeat values
print("\nUse set to remove repeated values")
for language in set(favorite_languages.values()):
    print(language.title())
