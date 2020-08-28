
# rules:
#	six digits
#	value within range of 153517-630395
#	subsequent digits never decrease
#	one double allowed

# use the fact that it's starting from 153517
#155678
#156789
#156678
#...

passes = []
def generatePass(num):
	# get the last digit
	t = str(num)
	if len(t) > 5:
		# check that there's a double in the password
		doubletest = False
		for c in range(1, len(t)):
			if t[c] == t[c - 1]:
				doubletest = True
		if doubletest:
			passes.append(num)
		return

	lastdigit = num % 10
	startpos = lastdigit
	for i in range(startpos, 10):
		nnum = num * 10
		generatePass(nnum + i)

for i in range(1,7):
	generatePass(i)
print(passes)

keep = []
for item in passes:
	if item > 153517 and item < 630395:
		keep.append(item)
print(keep)
print(len(keep))