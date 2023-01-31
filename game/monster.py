import random
from game.pickup import pickup
import math
class Monster:
  def __init__(self,name,raritypercent,health,armor,damage,loottable,amounttable1,amounttable2):
    self.rarity = raritypercent
    self.health = health
    self.loottable = loottable
    self.minarray = amounttable1
    self.maxarray = amounttable2
    self.name = name
    self.damage = damage
    self.armor = armor
    self.difficulty = ((self.damage*2) + self.health + 5*self.armor)
  def hit(self):
    return (random.randint(0,math.ceil(float(self.damage)/2.0)) + random.randint(0,math.floor(float(self.damage)/2.0)))
  def getHit(self, amount):
    final = amount
    final -= self.armor
    if final <= 0:
      final = 0
      print("You couldn't get through the " + self.name + "'s armor")
    else:
      print("You hit the " + self.name + " for " + str(final))
    self.health -= final
  def loot(self,player):
    givearray = []
    for i in range(len(self.loottable)):
      am = random.randint(self.minarray[i],self.maxarray[i])
      if am != 0:
        givearray.append({self.loottable[i]:am})
    for i in givearray:
      pickup({list(i.keys())[0]:i[list(i.keys())[0]]}, player.inventory, player1=player)
  def attack(self):
    if random.randint(0,100) < self.percenttohit:
      dam = self.hit()
      print("The " + self.name + " hit you for " + dam + " damage!")
      return dam
    else:
      print("The " + self.name + " missed you!")
      return 0