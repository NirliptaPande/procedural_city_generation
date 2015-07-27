def input_image_setup(img_name, img2_name):
	'''	Nimmt ein Bild als input, erstellt eine "Regel-Karte". Bei der Bild-
	erstellung bedenken: Rot = Gitter, Gruen = Verzweigt, Blau = Radial, wobei ein schwarzer
	Pixel ein Zentrum definiert. '''
	import matplotlib.image as mpimg
	
	#TODO:translate	
	
	img = mpimg.imread(img_name)
	img2 = mpimg.imread(img2_name)
	
	#IF PNG and not JPG, get numerical values right
	if img_name[len(img_name)-2]=='n':
		img*=255
	if img2_name[len(img2_name)-2]=='n':
		img2*=255
	
	return img, img2