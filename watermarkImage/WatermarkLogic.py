import PIL
from PIL import Image
import os
from watermark.Position import Position


def changeOpacity(logoImage, opacityNumber):
    try:
        if logoImage is None:
            raise Exception('Please choose logo first')
        logoImage.load()
        bands=list(logoImage.split())
        newImage = logoImage
        if len(bands) == 4:
            # Assuming alpha is the last band
            bands[3] = bands[3].point(lambda x: x*(opacityNumber/10))
            newImage = PIL.Image.merge(newImage.mode, bands)
        return newImage
    except Exception as e:
        print(e)


def getPosition(inputPosition, mbox, sbox):
    try:
        switcher = {
            1: (mbox[0] - sbox[0]-5, mbox[1] - sbox[1]-5),
            2: (mbox[2] - sbox[2]-5, mbox[1] - sbox[1]-5),
            3: (mbox[1] - sbox[1]-5, mbox[3] - sbox[3]-5),
            4: (mbox[2] - sbox[2]-5, mbox[3] - sbox[3]-5),
        }
        return switcher.get(inputPosition, (-12, -11))
    except Exception as e:
        print(e)


def addLogo(image1, image2, position, logoSize = 2):
    #print('water mark image: {} in position: {}, logo size: {}'.format(image1.filename, position, logoSize))
    mainImage = image1
    littleImage = image2

    size = numbersToLogoSize(logoSize)
    wsize = int(min(mainImage.size[0], mainImage.size[1]) * size)
    wpercent = (wsize / float(littleImage.size[0]))
    hsize = int((float(littleImage.size[1]) * float(wpercent)))

    simage = littleImage.resize((wsize, hsize))
    simage = simage.convert('RGBA')
    mbox = mainImage.getbbox()
    sbox = simage.getbbox()

    box = getPosition(int(position), mbox, sbox)
    mainImage.paste(simage, box, simage)
    return mainImage


def validateImage(imageName):
    return imageName.lower().endswith(".png") or imageName.lower().endswith(".jpg")

def saveImages(listOfImages, pathToSave):
    if not os.path.exists(pathToSave):
        os.makedirs(pathToSave)
    os.chdir(pathToSave)
    for image in listOfImages:
        newName = image.filename.split("\\")
        image.save(newName[len(newName)-1])

def numbersToLogoSize(userLogoSize):
    try:
        switcher = {
            1: 0.15,
            2: 0.25,
            3: 0.35,
            4: 0.45,
        }
        return switcher.get(userLogoSize, 0.25)
    except Exception as e:
        print(e)


def watermarkDir(dirToSearch, logo, position=Position.BOTTOM_RIGHT, opacity=5, logoSize=2):
    try:
        print('Starting paste logo in images...')
        listOfNewImages = []
        logoPathSplit = logo.filename.split("\\")
        logoName = logoPathSplit[len(logoPathSplit)-1]
        if not validateImage(logoName):
            raise ValueError("Logo image: {} must be PNG or JPG image".format(logo.filename))
        logo = changeOpacity(logo, opacity)
        for imageStr in os.listdir(dirToSearch):
            if validateImage(imageStr):
                image = PIL.Image.open(os.path.join(dirToSearch,imageStr))
                imageWithLogo = addLogo(image, logo, position, logoSize)
                listOfNewImages.append(imageWithLogo)

        print('Done !!!')
        return listOfNewImages
    except Exception as e:
        print('Something went wrong.')
        print(e.args)


def watermarkList(listOfImages, logo, position=Position.BOTTOM_RIGHT, opacity=5, logoSize=2):
    try:
        print('Starting paste logo in images...')
        listOfNewImages = []
        logoPathSplit = logo.filename.split("\\")
        logoName = logoPathSplit[len(logoPathSplit)-1]
        if not validateImage(logoName):
            raise ValueError("Logo image: {} must be PNG or JPG image".format(logo.filename))
        logo = changeOpacity(logo, opacity)

        for image in listOfImages:
            imageWithLogo = addLogo(image, logo, position, logoSize)
            listOfNewImages.append(imageWithLogo)

        print('Done !!!')
        return listOfNewImages
    except Exception as e:
        print('Something went wrong.')
        print(e.args)