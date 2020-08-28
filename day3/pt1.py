import math

class Point:
	x = 0
	y = 0

	def __init__(self, _x=0,_y=0):
		self.x = _x
		self.y = _y

	def print(self):
		print("(", self.x, ",", self.y, ")")

	def toTuple(self):
		return (self.x, self.y)

	def stepLeft(self):
		self.y -= 1

	def stepRight(self):
		self.y += 1

	def stepDown(self):
		self.x -= 1

	def stepUp(self):
		self.x += 1


def takeStep(direction, steps, currpos):
	if direction == "L":
		currpos.stepLeft()
	if direction == "R":
		currpos.stepRight()
	if direction == "U":
		currpos.stepUp()
	if direction == "D":
		currpos.stepDown()
	return steps - 1, currpos

def getAllPlaces(wire):
	places = set()
	currpos = Point(0,0)
	for movement in wire:
		direction = movement[0]
		steps = int(movement[1:])
		while steps > 0:
			steps, currpos = takeStep(direction, steps, currpos)
			#currpos.print()
			places.add(currpos.toTuple())
	return places

def getManhattan(tupleA, tupleB):
	return abs(tupleA[0] - tupleB[0]) + abs(tupleA[1] - tupleB[1])

def getClosestIntersections(wireA, wireB):
	placesA = getAllPlaces(wireA)
	placesB = getAllPlaces(wireB)
	#intersect the two sets
	intersects = placesA.intersection(placesB)
	mindist = 999999
	mindist_p = (mindist, mindist)
	for item in intersects:
		# calculate manhattan distance from point zero
		manh = getManhattan((0,0),item)
		if manh < mindist:
			mindist_p = item
			mindist = manh
	#print(mindist_p)
	#print(mindist)
	return mindist_p

def strtoWire(s):
	return s.split(",")

#assert getClosestIntersections(["R8","U5","L5","D3"], ["U7","R6","D4","L4"]) == (3,3)
wireA = strtoWire("R75,D30,R83,U83,L12,D49,R71,U7,L72")
wireB = strtoWire("U62,R66,U55,R34,D71,R55,D58,R83")
#print(getClosestIntersections(wireA, wireB))
print("all tests OK")

with open("input.txt","r") as inp:
	wireA = strtoWire(inp.readline())
	wireB = strtoWire(inp.readline())
	r = getClosestIntersections(wireA, wireB)
	print(r)
	print(getManhattan((0,0), r))