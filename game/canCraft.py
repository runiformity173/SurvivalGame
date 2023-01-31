from game.recipe import Recipe
def printMissing(dct):
  if len(dct) > 2:
    recipestr = ""
    for i in range(len(dct)-1):
      recipestr += (str(list(dct.values())[i]) + " " + str(list(dct.keys())[i]) + ", ")
    recipestr += ("and " + str(list(dct.values())[len(dct) - 1]) + " " + str(list(dct.keys())[len(dct) - 1]))
    print("You are missing " + recipestr + ".")
  elif len(dct) == 2:
    print("You are missing " + str(list(dct.values())[0]) + " " + list(dct.keys())[0] + " and " + str(list(dct.values())[1]) + " " + list(dct)[1] + ".")
  elif len(dct) == 1:
    print("You are missing " + str(list(dct.values())[0]) + " " + list(dct.keys())[0] + ".")
  else:
    print("Not missing any.")
  input("Enter to Close - ")
def canCraft(cra, player, amt):
  successes = 0
  dct = {}
  for i in range(len(cra.requiredArray)):
    for l in player.inventory:
      if l == cra.requiredArray[i] and player.inventory[l] >= (cra.amountsArray[i]*amt):
        successes += 1
      elif l == cra.requiredArray[i]:
        dct[cra.requiredArray[i]] = ((cra.amountsArray[i]*amt)-player.inventory[l])
    if cra.requiredArray[i] not in player.inventory:
      dct[cra.requiredArray[i]] = (cra.amountsArray[i]*amt)
  nt = 1
  if cra.workstation == "None":
    nt = 0
  else:
    if cra.workstation in player.workstations:
      successes += 1
    else:
      dct["Workstation"] = (cra.workstation).capitalize()
  if successes == len(cra.requiredArray)+nt:
    return True
  else:
    printMissing(dct)
    return False