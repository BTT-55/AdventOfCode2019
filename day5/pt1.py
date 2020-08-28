
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
#print(handleAction([1002,4,3,4,33]))
#simulateMachine([11103,1,4,1,99])
#print(handleAction([2,3,0,3,99]))