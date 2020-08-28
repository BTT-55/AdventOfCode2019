import math
import numpy as np

def getAsteroids(starmap):
	asteroids = []
	for row in range(len(starmap)):
		for column in range(len(starmap[row])):
			if starmap[row][column] == "#":
				asteroids.append((row, column))
	return asteroids

def getLaserPos(starmap):
	for i in range(len(starmap)):
		for j in range(len(starmap[i])):
			if starmap[i][j] == "X":
				return (i,j)
	return (-1,-1)

def getVisibleAsteroids(starmap, asteroids, las_x, las_y):
	checkset = set()
	visibles = []
	for asteroid in asteroids:
		# calculate the angle to the laser
		angle = math.degrees(math.atan2(las_x - asteroid[0], las_y - asteroid[1]))
		# now make sure that the angles are sorted correctly
		angle = (angle + 360 - 90) % 360
		if not angle in checkset:
			visibles.append((asteroid[0], asteroid[1], angle))
			checkset.add(angle)
	visibles.sort(key=lambda x:x[2])
	return visibles

def firing_until(starmap,stop_at):
	las_x, las_y = getLaserPos(starmap)
	print(las_x, las_y)

	# put all immediately visible asteroids in the line of fire
	asteroids_exploded = 0
	while True:
		# get all the asteroids left
		asteroids = getAsteroids(starmap)
		stop_at = min(stop_at, len(asteroids))
		if stop_at == 0:
			return
		# sort the asteroids based on their L2-distance from the laser
		asteroids.sort(key=lambda x: (x[0] - las_x) ** 2 + (x[1] - las_y) ** 2)

		# get all asteroids the laser can "see" right now
		visible_asteroids = getVisibleAsteroids(starmap, asteroids, las_x, las_y)
		# explode the asteroids visible, then prepare for another round
		for aster in visible_asteroids:
			asteroids_exploded += 1
			# vaporize that sucker
			starmap[aster[0]][aster[1]] = "!"
			#print(starmap)
			starmap[aster[0]][aster[1]] = "."
			print("Exploded asteroid",asteroids_exploded,"at (",aster[1],",",aster[0],")")
			if asteroids_exploded == stop_at:
				return aster[0], aster[1]

def main():	
	with open("input.txt", "r", encoding="utf-8") as inp:
		rawdata = inp.readlines()
		starmap = []
		for item in rawdata:
			row = []
			for i in item:
				if i == "." or i == "#" or i == "X":
					row.append(i)
			starmap.append(row)
		starmap[11][11] = "X"
		#print(starmap)
		firing_until(starmap,200)

main()