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

def getPixel(layers, pos_x, pos_y):
	# remember, 'layers' is arranged according to [['123','456'],['123','456']]
	for i in range(0, len(layers)):
		curr_layer = layers[i]
		curr = int(curr_layer[pos_y][pos_x])
		if curr != 2:
			return curr
	return 2

def toImage(layers, height, width):
	# alright, so.
	# make a matrix to put stuff in
	image = []
	for i in range(0, height):
		curr_bar = []
		for j in range(0, width):
			curr_bar.append(-1)
		image.append(curr_bar)

	for i in range(0, height):
		for j in range(0, width):
			# decide new pixel value
			image[i][j] = getPixel(layers, i, j)
	return image

def pixelToString(pixel):
	if pixel == 0:
		return " "
	else:
		return "1"

def printImage(img, height, width):
	with open("output.txt","w", encoding="utf-8") as outp:
		for i in range(height):
			for j in range(width):
				t = img[i][j]
				t = pixelToString(t)
				outp.write(t)
			outp.write("\n")

def printImageT(img, height, width):
	with open("outputT.txt","w", encoding="utf-8") as outp:
		for i in range(width):
			for j in range(height):
				t = img[j][i]
				t = pixelToString(t)
				outp.write(t)
			outp.write("\n")

def main():
	height = 25
	width = 6
	with open("input.txt", "r", encoding="utf-8") as inp:
		rawdata = inp.readline()
		layers = toLayers(rawdata, height, width)
		#print(layers)
		img = toImage(layers, height, width)
		#print(img)
		printImage( img, height, width)
		printImageT(img, height, width)

main()
#height = 2
#width = 3
#layers = toLayers("020202111111", height, width)
#print(layers)
#img = toImage(layers, height, width)
#print(img)