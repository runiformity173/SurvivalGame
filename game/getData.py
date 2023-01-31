import json
import os
from game.recipe import Recipe
from game.monster import Monster
# iterate over files in
# that directory
def getRecipes():
  #directories = ['data/recipes/armor','data/recipes/craftingMaterials','data/recipes/healing','data/recipes/tools','data/recipes/tools','data/recipes/tools','data/recipes/tools','data/recipes/workstations']
  final = []
  for directory in os.listdir("data/recipes"):
    for folder in os.listdir(os.path.join("data/recipes",directory)):
      f = os.path.join(directory, folder)
      for filename in os.listdir("data/recipes/" + f):
        with open(os.path.join("data/recipes",f,filename), "r") as fl:
          dict = json.load(fl)
        q = Recipe([],[],0,0,0,0,"",0)
        q.requiredArray = dict["requiredArray"]
        q.amountsArray = dict["amountsArray"]
        q.returns = dict["returns"]
        q.amount = dict["amount"]
        q.workstation = dict["workstation"]
        q.craftingTime = dict["Ptime"]
        q.props = dict["property"]
        if "damage" in q.props:
          q.damage = str(dict["damage"]).split(" ", 1)
        elif "armor" in q.props:
          q.damage = str(dict["damage"]).rsplit("|", 1)
        else:
          q.damage = dict["damage"]
        if "damage" in q.props:
          q.damage[0] = int(q.damage[0])
        final.append(q)
  return final
def getMonsters():
  directory = 'data/monsters'
  final = []
  for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    with open(f, "r") as fl:
      dict = json.load(fl)
    q = Monster("",0,0,0,0,[],[],[])
    q.rarity = dict["raritypercent"]
    q.health = dict["health"]
    q.loottable = dict["loottable"]
    q.minarray = dict["amounttable1"]
    q.maxarray = dict["amounttable2"]
    q.name = dict["name"]
    q.damage = dict["damage"]
    q.armor = dict["armor"]
    q.difficulty = ((q.damage*2) + q.health + 5*q.armor)
    final.append(q)
  return final
def getResources(ty):
  with open("data/resources.json", "r") as fl:
    dict = json.load(fl)
  if ty == "re":
    return dict["resources"]
  if ty == "ba":
    return dict["baseR"]
  if ty == "b":
    return dict["boostype"]
  if ty == "bm":
    return dict["boostamt"]