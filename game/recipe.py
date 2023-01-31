class Recipe:
	def __init__(self, requiredArray, amountsArray, returns, amount, Ptime, workstation, props, damage):
		self.requiredArray = requiredArray
		self.amountsArray = amountsArray
		self.returns = returns;self.props = props
		self.amount = amount
		self.workstation = workstation
		self.damage = damage;self.craftingTime = Ptime
def toStr(recipe):
  return (str(recipe.returns) + "(" + str(recipe.amount) + ")")