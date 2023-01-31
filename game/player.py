import time
from game.craftDone import craftDone
from game.getData import getRecipes
class Player:
  def __init__(self):
    self.inventory = {}
    self.health = 20
    self.armor = {"head": 0, "chest": 0, "feet": 0, "hands": 0}
    self.workstations = []
    self.damage = 1
    self.heal = 1
    self.crafts = {"done":{},"counts":{},"ending":{}}
    self.discovered = []
#Runs end of every action
  from game.pickup import pickup
  def __call__(self):
    toBeDelled = []
    for item in self.crafts["ending"]:
      if self.crafts["ending"][item] <= time.time():
        toBeDelled.append(item)
        tt = True
        for item2 in self.crafts["done"]:
          if item2 == item:
            self.crafts["done"][item] += self.crafts["counts"][item]
            tt = False
        if tt:
          self.crafts["done"][item] = self.crafts["counts"][item]
    for item in toBeDelled:
      del self.crafts["ending"][item]
      del self.crafts["counts"][item]
    t = list(self.crafts["done"].keys())
    recipeList = []
    for item in t:
      for i in getRecipes():
        if i.returns == item:
          recipeList.append(i)
    for item in range(len(t)):
      craftDone(recipeList[item],self.crafts["done"][t[item]],self)
      del self.crafts["done"][t[item]]
    toBeDelled = []
    for item in self.inventory:
      if self.inventory[item] == 0:
        toBeDelled.append(item)
    if len(toBeDelled) > 0:
      for item in toBeDelled:
        del self.inventory[item]
    if self.health > 20:
      self.health = 20
#Save and Load
  def toDict(self):
    final = {"inventory":self.inventory,"discovered":self.discovered,"health":self.health,"armor":self.armor,"heal":self.heal,"damage":self.damage,"workstations":self.workstations,"crafts":self.crafts}
    return final
  def damaged(self, amt):
    armorValue = 0
    for t in self.armor:
      armorValue += self.armor[t]
    se = (amt-armorValue)
    if se <= 0:
      se = 0
      self.health -= se
      print("You took no damage. You are still at " + str(self.health))
    else:
      self.health -= se
      print("You took " + str(se) + " damage, putting you at " + str(self.health))
def toPlayer(dict):
  final = Player()
  final.health = dict["health"]
  final.inventory = dict["inventory"]
  final.workstations = dict["workstations"]
  final.heal = dict["heal"]
  final.damage = dict["damage"]
  final.armor = dict["armor"]
  final.crafts = dict["crafts"]
  final.discovered = dict["discovered"]
  return final