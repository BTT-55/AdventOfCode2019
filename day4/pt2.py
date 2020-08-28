
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

def containsDoubleDigit(s):
	for c in range(1, len(s)):
		if s[c] == s[c - 1] and s[c] != "*":
			return int(s[c])
	return -1

def containsTripleDigit(s):
	for c in range(2, len(s)):
		if s[c] == s[c - 2] and s[c] != "*":
			return int(s[c])
	return -1

passes = []
def generatePass(num):
	# get the last digit
	t = str(num)
	if len(t) > 5:
		# check that there's a double in the password
		dup = containsTripleDigit(t)
		while dup != -1:
			# replace all occurences of dup with "x"
			t = t.replace(str(dup), "*")
			dup = containsTripleDigit(t)
		if containsDoubleDigit(t) != -1:
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