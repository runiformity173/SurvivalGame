from game.recipe import Recipe
from game.pickup import pickup
from game.player import *
from game.getData import *
import os.path
from os import path
import pickle
import json
import time
name = "saves/"+input("Save file name: ")+".json"
from game.action import action
if path.exists(name) == False:
  config_dictionary = (Player().toDict())
  with open(name, 'w') as config_dictionary_file:
    json.dump(config_dictionary, config_dictionary_file, indent=4)
with open(name, 'r') as config_dictionary_file:
  config_dictionary = json.load(config_dictionary_file)
  player = toPlayer(config_dictionary) 
recipes = getRecipes()
player()
while player.health > 0:
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")
  action(name, player, recipes)
  time.sleep(1)
print("You died!")