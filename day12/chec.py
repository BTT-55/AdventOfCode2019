
# OK.
# The N-Body Problem

class Moon:
	x = 0
	y = 0
	z = 0
	vx = 0
	vy = 0
	vz = 0

	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
		self.vx = 0
		self.vy = 0
		self.vz = 0

	def printMoon(self):
		print("<x: " + str(self.x), "y: " + str(self.y), "z: " + str(self.z), end="\t|\t")
		print("vx: " + str(self.vx), "vy: " + str(self.vy), "vz: " + str(self.vz) + ">")

	def getPotentialEnergy(self):
		return abs(self.x) + abs(self.y) + abs(self.z)

	def getKineticEnergy(self):
		return abs(self.vx) + abs(self.vy) + abs(self.vz)

def takeStep(moons):
	# first, apply gravity.
	for i in range(len(moons)):
		for j in range(i+1, len(moons)):
			moonA = moons[i]
			moonB = moons[j]
			# now we're guaranteed two different moons
			if moonA.x < moonB.x:
				moonA.vx += 1
				moonB.vx -= 1
			elif moonA.x > moonB.x:
				moonA.vx -= 1
				moonB.vx += 1
			if moonA.y < moonB.y:
				moonA.vy += 1
				moonB.vy -= 1
			elif moonA.y > moonB.y:
				moonA.vy -= 1
				moonB.vy += 1
			if moonA.z < moonB.z:
				moonA.vz += 1
				moonB.vz -= 1
			elif moonA.z > moonB.z:
				moonA.vz -= 1
				moonB.vz += 1
	# second, apply velocity to each moon
	for moon in moons:
		moon.x += moon.vx
		moon.y += moon.vy
		moon.z += moon.vz
	return moons

def printMoons(moons):
	for moon in moons:
		moon.printMoon()

def calculateTotalEnergy(moons):
	total = 0
	for moon in moons:
		total += moon.getPotentialEnergy() * moon.getKineticEnergy()
	print(total)
	return total

moons = []
moons.append(Moon(-1,0,2))
moons.append(Moon(2,-10,-7))
moons.append(Moon(4,-8,8))
moons.append(Moon(3,5,-1))
# alright, initialization complete
printMoons(moons)
steps = 126
for i in range(0, 126):
	moons = takeStep(moons)
	printMoons(moons)
	print("---------")