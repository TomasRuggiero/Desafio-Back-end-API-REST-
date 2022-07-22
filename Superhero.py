import json

with open('C:\heroes.json', 'r+') as f:
    heroes = json.load(f)

if not ('votes' in heroes[0]):
    with open('C:\heroes.json', 'w') as w:
        for hero in heroes:
            hero['votes'] = 0
        json.dump(heroes, w, indent=4)

currentVotes = heroes

while True:
    request = input('Insert request: "superhero": ')
    foundHero = False

    for hero in heroes:
        if request == hero['superhero']:
            foundHero = True
            hero['votes'] = int(hero['votes']) + 1
            with open('C:\heroes.json', 'w') as w:
                json.dump(heroes, w, indent=4)

            print('Superhero voted: ')
            printHero = hero
            del printHero['alter_ego']
            del printHero['first_appearance']
            print(hero)

    if foundHero:
        break
    else:
        print('Reenter request')


def bubble(lista):
    n = len(lista)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if int(lista[j]['votes']) < int(lista[j + 1]['votes']):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


bubble(heroes)

for hero in currentVotes:
    if hero['votes'] == 0:
        hero.clear()
    elif 'first_appearance' in hero: del hero['first_appearance']

i = len(currentVotes)
while currentVotes[i-1] == {}:
    currentVotes.pop(-1)
    i -= 1

print('Current Votes: ')
for hero in currentVotes:
    print(hero)

marvelVotes = 0
dcVotes = 0

publisherVotes = [{"publisher":"DC Comics",
      "votes": 0}, {"publisher":"Marvel Comics",
      "votes": 0}]

for hero in currentVotes:
    if hero['publisher'] == 'Marvel Comics': publisherVotes[1]['votes'] += hero['votes']
    elif hero['publisher'] == 'DC Comics': publisherVotes[0]['votes'] += hero['votes']

print('\n Votes per Publisher: ')
for publisher in publisherVotes:
    print(publisher)


