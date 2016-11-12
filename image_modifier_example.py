# note this code is neither complete nor correct; the PIL / numpy modules and their functions are correct though

from PIL import Image, ImageDraw
import numpy as np

class ImageModifier(object):
	def __init__(self, file):
		self.im = Image.open('path/to/file.jpg')
		self.pix = np.asarray(im)
	def modify(self,xy,color):
		pass

	def save(self,file):
		pass


n = np.asarray(im)

n[42,43] = [255, 255, 255]

im2 = Image.fromarray(n,dtype='uint8')

im2.save('modified_image.jpg')

modifier = ImageModifier('path/to/file.jpg')

modifier.modify((23,56),'black')
modifier.save('new_file.jpg')