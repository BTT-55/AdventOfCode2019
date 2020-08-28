# orbits
# if A orbits B and B orbits C, then A orbits C
# count direct and indirect orbits

class Orbited:
	name = ""
	children = []
	parent = None

	def __init__(self, name="", parent=None):
		self.name = name
		self.children = []
		self.parent = parent

	def setParent(self, parent):
		self.parent = parent

	def getParent(self):
		return self.parent

	def addChild(self, child):
		self.children.append(child)
		child.setParent(self)

	def calculateOrbitCount(self, fromParent=-1):
		nval = fromParent +1
		# orb_value is fromParent + 1
		total_orbcount = nval
		# count from the children, recursively (once they've finished calculating their children, etc)
		for c in self.children:
			total_orbcount += c.calculateOrbitCount(nval)
		return total_orbcount

	def print(self):
		if self.parent == None:
			print("None ->", self.name)
		else:
			print(self.parent.name, "->", self.name)
		for c in self.children:
			c.print()

def getFromDict(objs, name):
	if name in objs.keys():
		return objs[name]
	else:
		t = Orbited(name)
		objs[name] = t
		return t

def main():
	allObjects = {}
	with open("input.txt", 'r') as inp:
		for line in inp.readlines():
			# first off, split into orbitee and orbiter
			orbitee = getFromDict(allObjects, line.partition(")")[0])
			orbiter = getFromDict(allObjects, line.partition(")")[2][:-1])

			# set orbitee as parent, orbiter as child
			orbitee.addChild(orbiter)

	roots = []
	for orbitname in allObjects.keys():
		curr = allObjects[orbitname]
		if curr.getParent() == None:
			roots.append(curr)

	for curr in roots:
		curr.print()

	totalsum = 0
	for item in roots:
		totalsum += item.calculateOrbitCount()
	print(totalsum)

main()