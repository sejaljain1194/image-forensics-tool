#!/usr/bin/env python2.7
from PIL import Image, ImageChops, ImageEnhance
import sys, os.path

filename1 = sys.argv[1]
filename2 = sys.argv[2]

im1 = Image.open(filename1)
im2 = Image.open(filename2)


ela_im = ImageChops.difference(im1, im2)
extrema = ela_im.getextrema()
max_diff = max([ex[1] for ex in extrema])
if max_diff != 0:
	scale = 255.0/max_diff
	ela_im = ImageEnhance.Brightness(ela_im).enhance(scale)
	print "Maximum difference was %d" % (max_diff)
	ela_im.show()
	print "Image is Photoshopped or Edited"
else:
	print "Not Photoshopped! "
