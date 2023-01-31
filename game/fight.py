from game.player import Player
from game.monster import Monster
import random
import math
def fight(player, monster2):
  monster = monster2
  turn = 0
  choice = ""
  while player.health > 0 and monster.health > 0 and choice != "run":
    if turn == 0:
      choice = ""
      while len(choice) < 1 or choice[0] not in ["a","h","r"]:
        choice = input("Attack(" + str(player.damage) + "), Heal, or Run: ").lower()
        if len(choice) > 0:
          choice = choice[0]
      if choice == "h":
        player.health += player.heal
        player()
      if choice == "a":
        monste = (random.randint(0,math.ceil(float(player.damage)/2.0)) + random.randint(0,math.floor(float(player.damage)/2.0)))
        monster.getHit(monste)
      turn = 1
    if monster.health <= 0 or choice == "r":
      break
    if turn == 1:
      player.damaged(monster.hit())
      turn = 0
  if monster.health <= 0:
    monster2.loot(player)