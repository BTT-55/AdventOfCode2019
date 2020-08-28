import math

def calcFuel(mass):
	mass = math.floor(float(mass) / 3)
	mass -= 2
	if mass >= 0:
		t = calcFuel(mass)
		if t >= 0:
			mass += t
	return mass

def main():
	# read the file
	with open("input.txt", "r", encoding="utf-8") as inp:
		rawdata = inp.readlines()
		totalfuel = 0
		for item in rawdata:
			tFuel = calcFuel(int(item))
			#print(tFuel)
			totalfuel += tFuel
		print(totalfuel)

main()
#print(calcFuel(14))
#print(calcFuel(1969))
#print(calcFuel(100756))