#For options with varrying amounts of things
def simplePrint(ins, typed="or"):
  if len(ins) > 2:
    recipestr = ""
    for i in range(len(ins)-1):
      recipestr += (str(ins[i]) + ", ")
    recipestr += (typed + " " + str(ins[len(ins) - 1]) + ": ")
    return recipestr
  elif len(ins) == 2:
    return (ins[0] + " " + typed + " " + str(ins[1]) + ": ")
  elif len(ins) == 1:
    return ("Only " + str(ins[0]) + ": ")
  else:
    return "uhhh....."