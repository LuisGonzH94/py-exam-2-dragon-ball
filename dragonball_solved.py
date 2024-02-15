import requests

class Character:
  def __init__(self, data):
    self.id = data['id']
    self.name = data['name']
    self.gender = data['gender']
    self.race = data['race']
    self.maxKi = data['maxKi']
    self.transformations = []

  def __str__(self):
    return self.name

  def get_info(self):
    response = requests.get(f'https://dragonball-api.com/api/characters/{self.id}')
    data = response.json()
    self.transformations = data['transformations']

  def get_transformations(self):
    self.get_info()
    return [transformation['name'] for transformation in self.transformations]

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


class DragonBallAPI:
  def __init__(self):
    self.url = 'https://dragonball-api.com/api'

  def get_characters(self):
    response = requests.get(f'{self.url}/characters?limit=100')
    characters = response.json()
    return [Character(character) for character in characters['items']]

  def get_characters_names(self):
    return [str(character) for character in self.get_characters()]

  def get_characters_by_gender(self, gender):
    return [str(character) for character in self.get_characters() if character.gender == gender]

  def get_characters_by_race(self, race):
    return [str(character) for character in self.get_characters() if character.race == race]

  def get_planets(self):
    response = requests.get(f'{self.url}/planets?limit=100')
    planets = response.json()
    return [Planet(planet) for planet in planets['items']]

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

# Tests

api = DragonBallAPI()
print(f'*** Characters:')
print(api.get_characters_names())
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

nombre = goku + vegeta
print(nombre) # Output: 'Gokugeta'

