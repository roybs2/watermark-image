import watermarkImage.Logic
from watermarkImage.Position import Position
import os
from PIL import Image

dirToSearch = os.getcwd()
logoPath = dirToSearch + r'\Logo\logo.png'
# example with logo size = 2 and logo locate in bottom right corner
# This example search for jpg\png images in specific dir
def watermarkDirExample():
    with Image.open(logoPath) as logo:
        list = watermarkImage.Logic.watermarkDir(dirToSearch, logo)
        watermarkImage.Logic.saveImages(list, dirToSearch + '\\new1')


# example with logo size = 4 (biggest), opacity = 8 and logo locate in top left corner
# This function get list of PIL images.
def watermarkListExample():
    image1 = Image.open(r'image1.jpg')
    image2 = Image.open(r'image2.jpg')
    listOfImages = [image1, image2]
    with Image.open(logoPath) as logo:
        list = watermarkImage.Logic.watermarkList(listOfImages, logo, Position.TOP_LEFT, 8, 4)
        watermarkImage.Logic.saveImages(list, dirToSearch + '\\new2')


# watermarkListExample()
# watermarkDirExample()
