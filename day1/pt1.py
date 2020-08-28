import math

def calcFuel(mass):
	mass = math.floor(float(mass) / 3)
	mass -= 2
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