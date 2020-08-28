
# this version utilizes a lookup dictionary instead of relying on "actual" memory for the machine
# relative base is stored in arr[-1]

inps = []
outs = []

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

def handleAction(arr, pos, passed_input):
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
		inp = passed_input
		arr, inppos = getDest(arr,pos+1,command[2])
		arr[inppos] = int(inp)
		nextpos += 2
		return arr, nextpos
	if opcode == "04":
		global outs
		arr, inp = getParam(arr,pos+1,command[2])
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
	direction = 0
	# up = 0, right = 1, down = 2, left = 3
	position = (0,0)
	squares = {}
	squares[position] = 0
	while check:
		# run the machine
		arr, pos = handleAction(arr, pos, squares[position])
		global outs
		if len(outs) == 2:
			# first up, paint this square the right color
			squares[position] = outs[0]
			# second, turn right if given 1
			if outs[1] == 1:
				direction = (direction + 1) % 4
			if outs[1] == 0:
				direction = (direction + 3) % 4
			# move ahead
			if direction == 0:
				position = (position[0] - 1, position[1])
			if direction == 1:
				position = (position[0], position[1] + 1)
			if direction == 2:
				position = (position[0] + 1, position[1])
			if direction == 3:
				position = (position[0], position[1] - 1)
			# now check for the new input to be given
			if not position in squares:
				squares[position] = 0
			# reset the output
			outs = []
		#print(arr)
		# stop when 99 is given
		check = pos != -1
	#print(arr)
	print("Amount of squares touched at least once:", len(squares.keys()))
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