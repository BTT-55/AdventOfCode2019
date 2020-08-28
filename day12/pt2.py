import math

# OK.
# The N-Body Problem

class Moon:
	def __init__(self,x,y,z):
		self.pos = []
		self.pos.append(x)
		self.pos.append(y)
		self.pos.append(z)
		self.vel = []
		self.vel.append(0)
		self.vel.append(0)
		self.vel.append(0)

	def printMoon(self):
		print("<x: " + str(self.pos[0]), "y: " + str(self.pos[1]), "z: " + str(self.pos[2]), end="\t|\t")
		print("vx: " + str(self.vel[0]), "vy: " + str(self.vel[1]), "vz: " + str(self.vel[2]) + ">")

def takeStep(moons, axis):
	# first, apply gravity.
	for i in range(len(moons)):
		for j in range(i+1, len(moons)):
			moonA = moons[i]
			moonB = moons[j]
			# now we're guaranteed two different moons
			if moonA.pos[axis] < moonB.pos[axis]:
				moonA.vel[axis] += 1
				moonB.vel[axis] -= 1
			elif moonA.pos[axis] > moonB.pos[axis]:
				moonA.vel[axis] -= 1
				moonB.vel[axis] += 1
	# second, apply velocity to each moon
	for moon in moons:
		moon.pos[axis] += moon.vel[axis]
	return moons

def printMoons(moons):
	for i in range(0, len(moons)):
		moons[i].printMoon()

def findLoop(moons, axis):
	axisnames = ["x","y","z"]
	# find when the current axis loops, i.e. the state (x0, y0, z0, w0) has occured before
	checkset = set()
	# keep adding to the checkset every so often as a way to check for prior occurence
	state = (moons[0].pos[axis], moons[1].pos[axis], moons[2].pos[axis], moons[3].pos[axis], moons[0].vel[axis], moons[1].vel[axis], moons[2].vel[axis], moons[3].vel[axis])
	checkset.add(state)

	stepsSince = 0
	for i in range(10000000):
		moons = takeStep(moons, axis)
		stepsSince += 1
		state = (moons[0].pos[axis], moons[1].pos[axis], moons[2].pos[axis], moons[3].pos[axis], moons[0].vel[axis], moons[1].vel[axis], moons[2].vel[axis], moons[3].vel[axis])
		#print(state)
		if state in checkset:
			#print("Loop found! The", axisnames[axis] + "-axis loops at", i+1, "steps.")
			return stepsSince
		else:
			checkset.add(state)
	return 0

def lcm(a, b):
	return abs(a * b) // math.gcd(a,b)

moons = []
moons.append(Moon(10,15,7))
moons.append(Moon(15,10,0))
moons.append(Moon(20,12,3))
moons.append(Moon(0 ,-3,13))
# moons.append(Moon(-1,0,2))
# moons.append(Moon(2,-10,-7))
# moons.append(Moon(4,-8,8))
# moons.append(Moon(3,5,-1))
# alright, initialization complete
#printMoons(moons)
loops = [0,0,0]
loops[0] = findLoop(moons, 0)
loops[1] = findLoop(moons, 1)
loops[2] = findLoop(moons, 2)
print("Result:", lcm(lcm(loops[0],loops[1]),loops[2]))