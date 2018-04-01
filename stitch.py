# import the necessary packages
from supporting_files.panorama import Stitcher
import argparse
import imutils
import cv2

imageA = cv2.imread("images" + "\\" + "IMG1.jpg")
imageB = cv2.imread("images" + "\\" + "IMG2.jpg")

stitcher = Stitcher()
result= stitcher.stitch([imageA, imageB])
cv2.imwrite('result.jpg',result)
