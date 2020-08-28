
# let's make use of the rules a little.
# one little thing that struck me about the data that there is only one reaction that leads to a given material
# 		e.g. if there's a rule 1 A => 1 FUEL, there won't be another rule
# 		so as a result we can make use of some recursion.

def ruleToReaction(rule):
	material = rule.partition(" => ")[2].partition(" ")[2]
	# let the rule be handled later, we just want to search it for now
	return material

def rulesToDict(rules):
	matDict = {}
	for rule in rules:
		rule = rule.strip("\n")
		mat = ruleToReaction(rule)
		matDict[mat] = rule
	return matDict

totalNecessary = {}
stopDecomposing = False

def getFirstNegativeMat():
	for key in totalNecessary.keys():
		if key != "ORE" and totalNecessary[key] < 0:
			return key
	return None

def getOreCount(matDict):
	global totalNecessary
	global stopDecomposing

	# Step 0: check if recursion has ended

	# Step 1: pop the first item on the totalNecessary list
	mat = getFirstNegativeMat()
	if mat == None:
		stopDecomposing = True
		return
	needed = totalNecessary[mat]
	del totalNecessary[mat]
	currentRule = matDict[mat]

	# Step 2: check how many times we will need the current mat
	produced = int(currentRule.partition(" => ")[2].partition(" ")[0])
	while needed < 0:
		# run the recipe once every step
		inputs = currentRule.partition(" => ")[0].split(", ")
		for inp in inputs:
			# 7 A
			inputAmount = int(inp.partition(" ")[0])
			inputElement = inp.partition(" ")[2]
			if not inputElement in totalNecessary:
				totalNecessary[inputElement]  = 0
			totalNecessary[inputElement] -= inputAmount
		needed += produced
	if needed != 0:
		totalNecessary[mat] = needed

with open("input.txt", "r") as inp:
	rawdata = inp.readlines()
	matDict = rulesToDict(rawdata)
	totalNecessary["FUEL"] = -1
	while not stopDecomposing:
		getOreCount(matDict)
	one_fuel = totalNecessary["ORE"] * -1
	print(totalNecessary["ORE"] * -1)