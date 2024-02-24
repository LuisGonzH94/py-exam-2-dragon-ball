import requests

class Character:
    def __init__(self, info):
        self.info = info
        self.id = info['id']
        self.name = info['name']
        self.gender = info['gender']
        self.race = info['race']
        self.transformation = []
        self.maxKi = info['maxKi']
    
    def __str__(self):
        return self.name
    
    def get_info(self):
        response = requests.get(f'https://dragonball-api.com/api/characters/{self.id}')
        data = response.json()
        self.transformation = data['transformations']
        
    def get_transformations(self):
        self.get_info()
        return [transformation['name']for transformation in self.transformation]
    
    def __add__(self, other):
        return self.name[:4] + other.name[-4:]
    
class Planet:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.isDestroyed = data['isDestroyed']
        self.characters = []
    
    def __str__(self):
        return self.name
    
    def get_info(self):
        response = requests.get(f'https://dragonball-api.com/api/planets/{self.id}')
        data = response.json()
        self.characters = data['characters']

    def get_characters(self):
        self.get_info()
        return [str(Character(character)) for character in self.characters]
    
class DragonBallApi:
    def __init__(self):
        self.url = 'https://dragonball-api.com/api'
    
    def get_characters(self):
        response = requests.get(f'{self.url}/characters?limit=100')
        characters_data = response.json()
        # items = characters_data['items'] //previous option I had set to iterate characters['items']
        return [Character(character) for character in characters_data['items']]
    
    def get_characters_names(self):
        characters = self.get_characters()
        return [character.name for character in characters]
        # si no utilizaria la clase Character, entonces seria 'characters_names = [character['name] for character in items]'
    
    def get_characters_by_gender(self, gender):
        characters = self.get_characters()
        filtered_gender = [character.name for character in characters if gender == character.gender]
        return filtered_gender
    
    def get_characters_by_race(self, race):
        characters = self.get_characters()
        filtered_race = [character.name for character in characters if race == character.race]
        return filtered_race

    def get_planets(self):
        response = requests.get(f'{self.url}/planets?limit=100')
        planets = response.json()
        planet_items = planets['items']
        return [Planet(planet) for planet in planet_items]
    
    def get_planets_names(self):
        return [str(planet) for planet in self.get_planets()]
    
    def get_destroyed_planets(self):
        return [str(planet) for planet in self.get_planets() if planet.isDestroyed]

    def get_weakest(self):
        characters = self.get_characters()
        return [str(character) for character in characters if character.maxKi == "0"]

    def get_strongest(self):
        characters = self.get_characters()
        return [str(character) for character in characters if "Googolplex" in character.maxKi]
    
api = DragonBallApi()
print(f'*** Characters:')
print(api.get_characters_names())
print(api.get_characters_by_gender('Female'))
print(api.get_characters_by_race('Saiyan'))

print(f'*** Planets:')
print(api.get_planets_names())

print(f'*** Destroyed Planets:')
print(api.get_destroyed_planets())

print(f'*** Weakest Characters:')
print(api.get_weakest())

print(f'*** Strongest Characters:')
print(api.get_strongest())

characters = api.get_characters()
goku = characters[0]
vegeta = characters[1]
names = goku + vegeta
# print(names)
print(vegeta.get_transformations())