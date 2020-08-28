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

	def getAncestors(self):
		ancestors = {}
		curr = self.parent
		steps = 1
		while curr != None:
			ancestors[curr.name] = steps
			steps += 1
			curr = curr.getParent()
		return ancestors

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
			tmp = line.partition(")")[2]
			if tmp[-1] == "\n":
				tmp = tmp[:-1]
			orbiter = getFromDict(allObjects, tmp)

			# set orbitee as parent, orbiter as child
			orbitee.addChild(orbiter)

	# get the earliest common ancestor
	# this works because we're working with a tree, which means only a single parent
	#	there will never be a structure where it's faster to hop via siblings
	ancs_A = allObjects["YOU"].getAncestors()
	checkset = set(ancs_A.keys())
	ancs_B = allObjects["SAN"].getAncestors()
	commonancestors = []
	for i in ancs_B.keys():
		if i in checkset:
			commonancestors.append((i, ancs_A[i] + ancs_B[i] - 2))
	#print(commonancestors)

	commonancestors.sort(key=lambda x:x[1])
	print(commonancestors)

	#print(ancs_A)

main()