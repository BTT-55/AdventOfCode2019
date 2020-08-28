
# this version utilizes a lookup dictionary instead of relying on "actual" memory for the machine
# relative base is stored in arr[-1]

def getParam(arr, pos, mode):
	arr, npos = getDest(arr, pos, mode)
	if not npos in arr:
		arr[npos] = 0
	return arr, arr[npos]

def getDest(arr, pos, mode):
	if mode == "1":
		# immediate mode - store in current location
		return arr, pos
	if mode == "0":
		# position mode - store at pointed location
		if not pos in arr:
			arr[pos] = 0
		return arr, arr[pos]
	if mode == "2":
		# relative mode: store at current + the relative_base
		#print("Relative base:", arr[-1])
		#print("Pos:", pos)
		n_addr = arr[pos] + arr[-1]
		if n_addr not in arr:
			arr[n_addr] = 0
		return arr, n_addr
	return None, None

def handleAction(arr, pos=0):
	nextpos = pos

	# get the command
	command = str(arr[pos])
	while len(command) < 5:
		command = "0" + command

	opcode = command[3:]
	#print("Opcode:", opcode)
	if opcode == "99":
		# end the program peacefully
		return arr, -1
	if opcode == "01":
		arr, x = getParam(arr, pos+1, command[2])
		arr, y = getParam(arr, pos+2, command[1])
		arr, z = getDest(arr,  pos+3, command[0])
		arr[z] = x + y
		nextpos += 4
		return arr, nextpos
	if opcode == "02":
		arr, x = getParam(arr, pos+1, command[2])
		arr, y = getParam(arr, pos+2, command[1])
		arr, z = getDest(arr,  pos+3, command[0])
		arr[z] = x * y
		nextpos += 4
		return arr, nextpos
	if opcode == "03":
		inp = input(":")
		arr, inppos = getDest(arr,pos+1,command[2])
		arr[inppos] = int(inp)
		nextpos += 2
		return arr, nextpos
	if opcode == "04":
		arr, inp = getParam(arr,pos+1,command[2])
		print("Output:", inp)
		nextpos += 2
		return arr, nextpos
	if opcode == "05":
		# jump if true
		# can never jump to empty memory so we're safe here
		arr, x = getParam(arr, pos+1, command[2])
		if x != 0:
			arr, nextpos = getParam(arr, pos+2, command[1])
		else:
			nextpos += 3
		return arr, nextpos
	if opcode == "06":
		# jump if false
		# can never jump to empty memory so we're safe here
		arr, x = getParam(arr, pos+1, command[2])
		if x == 0:
			arr, nextpos = getParam(arr, pos+2, command[1])
		else:
			nextpos += 3	
		return arr, nextpos
	if opcode == "07":
		# less than
		# doesn't jump so we're safe
		arr, x = getParam(arr, pos+1, command[2])
		arr, y = getParam(arr, pos+2, command[1])
		arr, z = getDest(arr,  pos+3, command[0])
		t = 0
		if x < y:
			t = 1
		arr[z] = t
		nextpos += 4
		return arr, nextpos
	if opcode == "08":
		# less than
		# doesn't jump
		arr, x = getParam(arr, pos+1, command[2])
		arr, y = getParam(arr, pos+2, command[1])
		arr, z = getDest(arr,  pos+3, command[0])
		t = 0
		if x == y:
			t = 1
		arr[z] = t
		nextpos += 4
		return arr, nextpos
	if opcode == "09":
		# modify relative base
		arr, nbase = getParam(arr, pos+1, command[2])
		arr[-1] += nbase
		nextpos += 2
		return arr, nextpos
	#print(arr)
	print("Encountered flawed code!!")
	print("Opcode:", opcode)
	return None, -1

def simulateMachine(arr):
	check = True
	pos = 0
	while check:
		# run the machine
		arr, pos = handleAction(arr, pos)
		#print(arr)
		check = pos != -1
	#print(arr)
	return arr

def toDict(arr):
	narr = {}
	narr[-1] = 0
	for i in range(0, len(arr)):
		narr[i] = arr[i]
	# initialize relative base
	return narr

def main():
	with open("input.txt", "r", encoding="utf-8") as inp:
		rawdata = inp.readline().split(",")
		arr = []
		for item in rawdata:
			arr.append(int(item))
		dic = toDict(arr)
		#print(dic)
		simulateMachine(dic)

main()

#t = toDict([106,0,4,99,104,9999,99])
#t = toDict([105,1,4,99,104,9999,99])
#t = toDict([109,234,203,55,204,55,99])
#t = toDict([104,1125899906842624,99])
#t = toDict([1101,99,99,234,99])
#simulateMachine(t)
#	input number, if less than 8 give 1, if not give 0

#simulateMachine([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9])
#	input number, if zero output 0 else 1