
def handleAction(arr, pos=0):
	if pos < 0 or pos > len(arr) or arr[pos] == 99:
		return arr

	curr = arr[pos] #opcode
	x = arr[arr[pos+1]]
	y = arr[arr[pos+2]]
	t = -1
	if curr == 1:
		t = x + y
	if curr == 2:
		t = x * y
	arr[arr[pos+3]] = t
	#print(arr)
	return handleAction(arr, pos + 4)

def main():
	with open("input.txt", "r", encoding="utf-8") as inp:
		rawdata = inp.readline().split(",")
		arr = []
		for item in rawdata:
			arr.append(int(item))
		print(arr)
		arr[1] = 12
		arr[2] = 2
		print(handleAction(arr))

main()
#print(handleAction([1,9,10,3,2,3,11,0,99,30,40,50]))
#print(handleAction([1,0,0,0,99]))
#print(handleAction([2,3,0,3,99]))