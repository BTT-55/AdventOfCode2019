# each layer of the "image" is 
def toSingleLayer(layer, height, width):
	curr = []
	while len(layer) > 0:
		curr.append(layer[:height])
		layer = layer[height:]
	return curr

# partition into individual layers
def toLayers(img, height, width):
	t = str(img)
	layers = []
	layerlen = height * width
	while len(t) > 0:
		curr_layer = t[:layerlen]
		layers.append(toSingleLayer(curr_layer, height, width))
		t = t[layerlen:]
	return layers

def countDigits(layer, digit):
	count = 0
	for p in layer:
		for p_2 in p:
			for p_3 in p_2:
				if p_3 == digit:
					count += 1
	return count

def main():
	with open("input.txt", "r", encoding="utf-8") as inp:
		rawdata = inp.readline()
		layers = toLayers(rawdata, 25, 6)
		print(layers)
		min_zeroes = 999999
		min_layer = min_zeroes
		for i in range(0, len(layers)):
			n_min = countDigits(layers[i],"0")
			if n_min < min_zeroes:
				min_zeroes = n_min
				min_layer = i
		print("Layer with least 0s is", min_layer)
		result = countDigits(layers[min_layer],"1") * countDigits(layers[min_layer],"2")
		print(result)


main()