import math
import copy

class Point:
	x = 0
	y = 0
	stepsSoFar = 0

	def __init__(self, _x=0,_y=0):
		self.x = _x
		self.y = _y

	def print(self):
		print("(", self.x, ",", self.y, ")")

	def toTuple(self):
		return (self.x, self.y)

	def getSteps(self):
		return self.stepsSoFar

	def stepLeft(self):
		self.y -= 1
		self.stepsSoFar += 1

	def stepRight(self):
		self.y += 1
		self.stepsSoFar += 1

	def stepDown(self):
		self.x -= 1
		self.stepsSoFar += 1

	def stepUp(self):
		self.x += 1
		self.stepsSoFar += 1


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
	places = {}
	currpos = Point(0,0)
	for movement in wire:
		direction = movement[0]
		steps = int(movement[1:])
		while steps > 0:
			steps, currpos = takeStep(direction, steps, currpos)
			#currpos.print()
			places[currpos.toTuple()] = currpos.getSteps()
	return places

def getManhattan(tupleA, tupleB):
	return abs(tupleA[0] - tupleB[0]) + abs(tupleA[1] - tupleB[1])

def getIntersections(wireA, wireB):
	placesA = getAllPlaces(wireA)
	placesB = getAllPlaces(wireB)

	# now find every intersection
	checkset = set()
	for item in placesA.keys():
		checkset.add((item[0], item[1]))
	inters = []
	for item in placesB.keys():
		tup = (item[0], item[1])
		if tup in checkset:
			sumSteps = placesA[tup] + placesB[tup]
			inters.append((item[0], item[1], sumSteps))
	return inters

def getClosestIntersections(wireA, wireB):
	inters = getIntersections(wireA, wireB)
	print(inters)

	inters.sort(key=lambda x:x[2])
	print(inters)

	return inters[0]

def strtoWire(s):
	return s.split(",")

#wireA = strtoWire("R75,D30,R83,U83,L12,D49,R71,U7,L72")
#wireB = strtoWire("U62,R66,U55,R34,D71,R55,D58,R83")
#getClosestIntersections(wireA, wireB)

with open("input.txt","r") as inp:
	wireA = strtoWire(inp.readline())
	wireB = strtoWire(inp.readline())
	r = getClosestIntersections(wireA, wireB)
	print(r)