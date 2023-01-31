from game.recipe import Recipe
from game.pickup import pickup
def craftDone(recipe,amt, player):
  i = recipe
  if i.props not in ["heal","armor","workstation"]:
    pickup({i.returns: (i.amount*amt)}, player.inventory, player1=player)
  if "damage" in i.props and i.damage[0] > player.damage:
    player.damage = i.damage[0]
    print("Your damage is now " + str(player.damage) +".")
  if "replace" in i.props:
    nkeys = list(player.inventory.keys())
    n = []
    c = []
    for k in nkeys:
      n.append(k.lower())
    for item in player.discovered:
      c.append(item.lower())
    if i.damage[1] in n:
      player.inventory[nkeys[n.index(i.damage[1])]] -= 1
      print("Replaced 1 " + i.damage[1])
    elif i.damage[1] not in c and i.damage[1] != "None":
      l = i.damage[1].split()
      for w in range(len(l)):
        l[w] = l[w].capitalize()
      ww = " ".join(l)
      player.discovered.append(ww)
  if i.props == "heal" and i.damage > player.heal:
    player.heal = i.damage
    print("Your healing ability is now " + str(player.heal) +".")
  if "armor" in i.props and int(i.damage[0].rsplit(' ', 1)[1]) > player.armor[i.damage[0].rsplit(' ', 1)[0]]:
    if i.returns not in player.discovered:
      player.discovered.append(i.returns)
    player.armor[i.damage[0].rsplit(' ', 1)[0]] = int(i.damage[0].rsplit(' ', 1)[1])
    print("Your " + i.damage[0].rsplit(' ', 1)[0] + " armor is now " + str(i.damage[0].rsplit(' ', 1)[1]) +".")
  if i.props == "workstation":
    if i.returns not in player.discovered:
      player.discovered.append(i.returns)
    print("You got the " + i.returns + " workstation.")
    player.workstations.append(i.returns)
  if i.returns not in player.discovered:
    player.discovered.append(i.returns)