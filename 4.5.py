rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']

for rabbit in rabbits:
    print(rabbit)

word = 'cat'
for letter in word:
    print(letter)

accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
for card in accusation.keys():
    print(card)

for card in accusation.values():
    print(card)

for item in accusation.items():
    print(item)

for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)

