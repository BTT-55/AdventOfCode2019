
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

outs = []
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
		#print("Output:", inp)
		global outs
		outs.append(inp)
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

def prettyPrintScreen(screen):
	for i in range(0, len(screen)):
		for j in range(0, len(screen[i])):
			t = screen[i][j]
			if t == 0:
				t = " "
			if t == 2:
				t = "w"
			if t == 3:
				t = "="
			if t == 4:
				t = "o"
			print(t, end="")
		print("")

def main():
	with open("input.txt", "r", encoding="utf-8") as inp:
		rawdata = inp.readline().split(",")
		arr = []
		for item in rawdata:
			arr.append(int(item))
		dic = toDict(arr)
		#print(dic)
		simulateMachine(dic)
	# ok, now draw the screen
	# dimensions of the screen are x = 35, y = 23
	screen = []
	for i in range(0,24):
		curr = []
		for j in range(0, 36):
			curr.append(0)
		screen.append(curr)
	# interpret the screen
	i = 0
	global outs
	while i < len(outs):
		screen[outs[i+1]][outs[i]] = outs[i+2]
		#print(screen)
		i += 3
	blockcount = 0
	for row in screen:
		for column in row:
			if column == 2:
				blockcount += 1
	prettyPrintScreen(screen)
	print("Total amount of blocks:", blockcount)


main()