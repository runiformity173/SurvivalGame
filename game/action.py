import time
from numpy import rec
from game.craftHelp import craft
from game.save import save
from game.pickup import pickup
from game.getData import *
from game.fight import fight
from game.simplePrint import simplePrint
import random
oldin = input
def input(prompt=""):
  final = oldin(prompt)
  if len(final) < 1:
    final = " "
  return final
def sortMonsters(t):
  return t.difficulty
def ninput(text):
  print(text)
  final = input()
  return final
def action(name, you, recipes):
  choice = input("See inventory, Craft, Gather, Heal, or Fight: ").lower()
  if len(choice) < 1:
    choice = " "
  if choice[0] == "h" or choice == "heal":
    you.health += you.heal
    if you.health > 20:
      you.health = 20
    print("You healed for " + str(you.heal) + ". You are now at " + str(you.health) + ".")
  if choice[0] == "c" or choice == "craft":
    newRec = []
    recipestr = ""
    if you.discovered == []:
      recipestr = "You don't know any recipes yet - "
    else:
      newRec = []
      newR = []
      for i in range(len(recipes)):
        pc = True
        for item in recipes[i].requiredArray:
          if item not in list(you.discovered):
            pc = False
        if recipes[i].returns in you.discovered and ("replace" in recipes[i].props or "armor" in recipes[i].props or "heal" in recipes[i].props or "workstation" in recipes[i].props):
          pc = False
        if pc:
          newRec.append(recipes[i])
          newR.append(recipes[i].returns)
      for i in range(len(recipes)):
        if recipes[i].returns in you.discovered and "replace" in recipes[i].props:
          cc = recipes[i].damage[1].split(" ")
          for word in range(len(cc)):
            cc[word] = cc[word].capitalize()
          cc = " ".join(cc)
          if cc in newR:
            fc = newR.index(cc)
            del newR[fc]
            del newRec[fc]
      for i in range(len(newRec)-1):
        recipestr += (str(newRec[i].returns) + ", ")
      recipestr += ("or " + str(newRec[len(newRec)-1].returns) + ": ")
    choice2 = ninput(recipestr)
    tt = choice2
    amt = 1
    n = True
    for c in tt.split(" ")[0]:
      if c not in ["1","2","3","4","5","6","7","8","9","0"]:
        n = False
      if len(c) < 1:
        n = False
    if n and (tt.split(" ") == [""] or tt.split(" ") == ["",""]):
      n = False
    if n:
      if int(tt.split(" ")[0]) <= 0:
        n = False
    if n:
      amt = int(tt.split(" ")[0])
      choice2 = tt.split(" ",1)[1]
    craft(you,choice2,recipes,amt)
  if choice == "see invintery":
    for item in you.inventory:
      you.inventory[item] *= 2
  if "see" in choice or choice[0] == "s":
    if len(you.inventory) > 2:
      recipestr = ""
      for i in range(len(you.inventory)-1):
        recipestr += (str(list(you.inventory.values())[i]) + " " + str(list(you.inventory.keys())[i]) + ", ")
      recipestr += ("and " + str(list(you.inventory.values())[len(you.inventory) - 1]) + " " + str(list(you.inventory.keys())[len(you.inventory) - 1]))
      print("You have " + recipestr + ".")
    elif len(you.inventory) == 2:
      print("You have " + str(list(you.inventory.values())[0]) + " " + list(you.inventory.keys())[0] + " and " + str(list(you.inventory.values())[1]) + " " + list(you.inventory)[1] + ".")
    elif len(you.inventory) == 1:
      print("You have " + str(list(you.inventory.values())[0]) + " " + list(you.inventory.keys())[0] + ".")
    else:
      print("You have nothing in your inventory.")
    choice3 = input("number/\"all\" itemName to drop Items, Enter to Close - ")
    if choice3 == "":
      choice3 = "0 nothing"
    if " " in choice3 and choice3.split(" ",1)[1].title() in list(you.inventory.keys()):
      if choice3.split(" ",1)[0].isnumeric():
        print("Dropped " + str(choice3.split(" ",1)[0]) + " " + choice3.split(" ",1)[1].title())
        you.inventory[choice3.split(" ",1)[1].title()] -= int(choice3.split(" ",1)[0])
      if choice3.split(" ",1)[0].lower() == "all":
        print("Dropped " + str(you.inventory[choice3.split(" ",1)[1].title()]) + " " + choice3.split(" ",1)[1].title())
        you.inventory[choice3.split(" ",1)[1].title()] = 0
  if choice[0] == "f" or choice == "fight":
    prompt = "You(" + str(you.damage*2 + 20 + (5*(you.armor["head"] + you.armor["hands"] + you.armor["chest"] + you.armor["feet"]))) + ") vs. "
    monsters = getMonsters()
    monsters.sort(key=sortMonsters)
    for t in range(len(monsters)-1):
      monster = monsters[t]
      difficulty = ((monster.damage*2) + monster.health + 5*monster.armor)
      prompt += monster.name + "(" + str(difficulty) + "), "
    t = len(monsters)-1
    monster = monsters[t]
    difficulty = ((monster.damage*2) + monster.health + 5*monster.armor)
    prompt += ("or " + monster.name + "(" + str(difficulty) + "): ")
    choice2 = ninput(prompt).lower()
    done2 = False
    for monster in monsters:
      if monster.name.lower()[0] == choice2[0] and not done2:
        done2 = True
        theMonster = monster
        fight(you,theMonster)
  if choice[0] == "g" or choice == "gather":
    resources = []
    for h in range(len(getResources("b"))):
      if getResources("ba")[h] <= 0:
        for item in list(you.inventory.keys()):
          if item in getResources("b")[h] and getResources("re")[h] not in resources:
            resources.append(getResources("re")[h])
      else:
        resources.append(getResources("re")[h])
    choice2 = input(simplePrint(resources))
    if len(choice2) < 1:
      choice2 = " "
    for i in range(len(resources)):
      if choice2.lower()[0] == resources[i].lower()[0]:
        tl = getResources("ba")[i]
        for v in reversed(getResources("b")[i]):
          for item in you.inventory:
            if v in item and (getResources("ba")[i]+getResources("bm")[i][getResources("b")[i].index(v)] > tl):
              tl = getResources("ba")[i] + getResources("bm")[i][getResources("b")[i].index(v)]
        if tl > 0:
          t = random.randint(0,tl)
          pickup({resources[i]:t}, you.inventory, player1=you)
  you()
  save(name, you)