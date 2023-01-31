import pickle
from game.player import Player
#with open('player', 'rb') as config_dictionary_file:
 # config_dictionary = pickle.load(config_dictionary_file)
#  print(config_dictionary.health)  
import json
def save(name, character):
  config_dictionary = character.toDict()
  with open(name, 'w') as config_dictionary_file:
    json.dump(config_dictionary, config_dictionary_file, indent=4)