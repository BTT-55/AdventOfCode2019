import math
import numpy as np

# Rules for this round:
#	get an asteroid map

def findMaxVisible(starmap):
	asteroids = []
	for row in range(len(starmap)):
		for column in range(len(starmap[row])):
			if starmap[row][column] == "#":
				asteroids.append((row, column))

	maxasters = 0
	maxaster_x = 0
	maxaster_y = 0
	for ast1 in asteroids:
		angles = set()
		for ast2 in asteroids:
			if ast1 == ast2:
				continue
			# else check angle
			angle = math.atan2(ast1[0] - ast2[0], ast1[1] - ast2[1])
			if not angle in angles:
				angles.add(angle)
		asters_visible = len(angles)
		if asters_visible > maxasters:
			maxasters = asters_visible
			maxaster_x = ast1[0]
			maxaster_y = ast1[1]
	print(maxaster_x, maxaster_y)
	print(maxasters)
	return maxasters

def stringtoStarMap(st, length):
	starmap = []
	while len(st) > 0:
		# carve off a bit of the string
		curr = st[:length]
		row = []
		for item in curr:
			row.append(item)
		starmap.append(row)
		st = st[length:]
	return np.transpose(starmap)

def main():	
	with open("input.txt", "r", encoding="utf-8") as inp:
		rawdata = inp.readlines()
		findMaxVisible(rawdata)

main()