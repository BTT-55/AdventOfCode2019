
def getParam(arr, pos, mode):
	if mode == "1":
		# immediate mode
		return arr[pos]
	if mode == "0":
		# position mode
		return arr[arr[pos]]

def getDest(arr, pos, mode):
	if mode == "1":
		# immediate mode - store in current location
		return pos
	if mode == "0":
		# position mode - store at pointed location
		return arr[pos]

def handleAction(arr, pos=0):
	if pos < 0 or pos > len(arr):
		print("Encountered error.")
		return None, -1
	if arr[pos] == 99:
		print("Program succesfully ended.")
		return arr, -1

	nextpos = pos

	# get the command
	command = str(arr[pos])
	while len(command) < 5:
		command = "0" + command

	opcode = command[3:]
	if opcode == "01":
		x = getParam(arr, pos+1, command[2])
		y = getParam(arr, pos+2, command[1])
		z = getDest(arr,  pos+3, command[0])
		arr[z] = x + y
		nextpos += 4
	if opcode == "02":
		x = getParam(arr, pos+1, command[2])
		y = getParam(arr, pos+2, command[1])
		z = getDest(arr,  pos+3, command[0])
		arr[z] = x * y
		nextpos += 4
	if opcode == "03":
		inp = input(":")
		inppos = getDest(arr,pos+1,command[2])
		arr[inppos] = int(inp)
		nextpos += 2
	if opcode == "04":
		inppos = getDest(arr,pos+1,command[2])
		print(arr[inppos])
		nextpos += 2
	if opcode == "05":
		# jump if true
		x = getParam(arr, pos+1, command[2])
		if x != 0:
			nextpos = getParam(arr, pos+2, command[1])
		else:
			nextpos += 3
	if opcode == "06":
		# jump if false
		x = getParam(arr, pos+1, command[2])
		if x == 0:
			nextpos = getParam(arr, pos+2, command[1])
		else:
			nextpos += 3	
	if opcode == "07":
		# less than
		x = getParam(arr, pos+1, command[2])
		y = getParam(arr, pos+2, command[1])
		z = getDest(arr,  pos+3, command[0])
		if x < y:
			arr[z] = 1
		else:
			arr[z] = 0
		nextpos += 4
	if opcode == "08":
		# less than
		x = getParam(arr, pos+1, command[2])
		y = getParam(arr, pos+2, command[1])
		z = getDest(arr,  pos+3, command[0])
		if x == y:
			arr[z] = 1
		else:
			arr[z] = 0
		nextpos += 4
	#print(arr)
	return arr, nextpos

def simulateMachine(arr):
	check = True
	pos = 0
	while check:
		# run the machine
		arr, pos = handleAction(arr, pos)
		check = pos != -1
	return arr

def main():
	with open("input.txt", "r", encoding="utf-8") as inp:
		rawdata = inp.readline().split(",")
		arr = []
		for item in rawdata:
			arr.append(int(item))
		print(arr)
		simulateMachine(arr)

main()

#simulateMachine([3,9,8,9,10,9,4,9,99,-1,8])
# input number, if == 8 give 1, if != 8 give 0

#simulateMachine([3,9,7,9,10,9,4,9,99,-1,8])
#	input number, if less than 8 give 1, if not give 0

#simulateMachine([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9])
#	input number, if zero output 0 else 1