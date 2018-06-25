__author__ = 'Sejal Jain'
# Modified version of the code by rahmatnazali 
# Original code available at https://github.com/rahmatnazali/image-copy-move-detection
# Last modified 23 June 2018

import os
import time
import ImageObject

def detect(imagefilename, blockSize=32):
    """
    Detects an image under a specific directory
    :param sourceDirectory: directory that contains images to be detected
    :param fileName: name of the image file to be detected
    :param outputDirectory: output directory
    :param blockSize: the block size of the image pointer (eg. 32, 64, 128)
    The smaller the block size, the more accurate the result is, but takes more time, vice versa.
    :return: None
    """

    singleImage = ImageObject.ImageObject(imagefilename, blockSize)
    status = singleImage.run()

    print "Image checked for copy-move editings."
    return status
