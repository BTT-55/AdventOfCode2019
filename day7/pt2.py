import copy

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

def handleAction(arr, pos, phase_setting, input_signal, phase_set):
	if arr[pos] == 99:
		#print("Program succesfully ended.")
		return arr, -1, None, False

	nextpos = pos
	output_signal = None

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
		if not phase_set:
			inp = phase_setting
			phase_set = True
		else:
			inp = input_signal
		inppos = getDest(arr,pos+1,command[2])
		arr[inppos] = int(inp)
		nextpos += 2
	if opcode == "04":
		inppos = getDest(arr,pos+1,command[2])
		print(arr[inppos])
		output_signal = arr[inppos]
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
	return arr, nextpos, output_signal, phase_set

def simulateMachine(arr, phase_setting, input_signal):
	check = True
	pos = 0
	output_signal = None
	phase_set = False
	while check:
		# run the machine
		arr, pos, t_out, phase_set = handleAction(arr, pos, phase_setting, input_signal, phase_set)
		check = pos != -1
		if t_out != None:
			output_signal = t_out
	return output_signal

def test_permutation(arr, permutation):
	input_signal = 0
	amps = []
	phases = []
	pos_list = []
	for i in range(0, 5):
		amps.append(copy.deepcopy(arr))
		phases.append(False)
		pos_list.append(0)
	stop = False

	curr_amp = 0
	signal = 0
	while not stop:
		# get current amp
		curr_arr = amps[curr_amp]
		pos = pos_list[curr_amp]
		phase_set = phases[curr_amp]
		phase_setting = permutation[curr_amp]
		# run until opcode 4 or 99
		run_OK = True
		while run_OK:
			# run a step of the program
			curr_arr, pos, t_sig, phase_set = handleAction(arr, pos, phase_setting, signal, phase_set)
			change_amp = False
			if t_sig != None:
				# then opcode 4 was just called
				signal = t_sig
				change_amp = True
			if pos == -1:
				# if we're on amp 5, stop running altogether and output the signal
				if curr_amp == 4:
					stop = True
				change_amp = True
			if change_amp:
				# move onto next amp
				amps[curr_amp] = curr_arr
				pos_list[curr_amp] = pos
				phases[curr_amp] = phase_set
				curr_amp = (curr_amp + 1) % 5
				run_OK = False
	return signal

from itertools import permutations

def main():
	with open("input.txt", "r", encoding="utf-8") as inp:
		rawdata = inp.readline().split(",")
		arr = []
		for item in rawdata:
			arr.append(int(item))
		print(arr)

		# challenge this time: run five serial programs
		phase_setting = [5,6,7,8,9]
		perm = permutations(phase_setting, 5)
		maxi = 0
		maxi_perm = phase_setting
		for i in list(perm):
			t = test_permutation(arr, i)
			if t > maxi:
				maxi = t
				maxi_perm = i
		print(maxi)
		print(maxi_perm)

main()

#simulateMachine([3,9,8,9,10,9,4,9,99,-1,8])
# input number, if == 8 give 1, if != 8 give 0

#simulateMachine([3,9,7,9,10,9,4,9,99,-1,8])
#	input number, if less than 8 give 1, if not give 0

#simulateMachine([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9])
#	input number, if zero output 0 else 1