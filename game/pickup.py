#from game.player import Player
def pickup(new, c, player1=None):
  if list(new.values())[0] > 0:
    print("You got " + str(list(new.values())[0]) + " " + list(new.keys())[0])
  placeholder = True
  cycles = len(c)
  for i in c:
    if placeholder:
      if i == list(new.keys())[0]:
        c[i] += list(new.values())[0]
        placeholder = False
  if placeholder:
    c[list(new.keys())[0]] = list(new.values())[0]
  if player1 != None:
    if list(new.keys())[0] not in player1.discovered:
      player1.discovered.append(list(new.keys())[0])