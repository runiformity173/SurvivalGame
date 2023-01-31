from game.recipe import Recipe
from game.canCraft import canCraft
from game.pickup import pickup
import time
from time import time
def craft(player, string, recipes, amt):
  for i in recipes:
    if i.returns.lower() == string.lower():
      if canCraft(i, player, amt):
        for l in range(len(i.requiredArray)):
          for p in player.inventory:
            if p == i.requiredArray[l]:
              player.inventory[p] -= i.amountsArray[l]*amt
        print("Crafting " + str(amt) + " " + i.returns)
        if i.returns not in player.crafts["ending"]:
          player.crafts["ending"][i.returns] = time() + float(i.craftingTime*amt)
          player.crafts["counts"][i.returns] = amt*i.amount
        else:
          player.crafts["counts"][i.returns] += amt*i.amount