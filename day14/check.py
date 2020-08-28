
checkset = set()
with open("input.txt","r") as inp:
	rawdata = inp.readlines()
	for item in rawdata:
		outp = item.partition(" => ")[2].partition(" ")[2]
		if outp in checkset:
			print("Duplicate detected!")
		else:
			checkset.add(outp)
print("checkset:", checkset)