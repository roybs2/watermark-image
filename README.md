Welcome to Watermark Image!

This package is written in python 3.5.4

The package will let you watermark batch of images.

# Installation:

You can install the watermark-image from PyPI:

    - pip install watermark-image 

# How to use:

You have 3 methods you can use:

1. watermarkDir:

    **input:**
    
        - dirToSearch: path to folder with all the images you want to watermark.
        - logo: PIL image object.
        - Position: one of 4 corners - please use Position enum from the package!
        - Opacity: opacity of logo (1-10), the default is 5.
        - Logo size: there are 4 sizes to choose, the default is 2. 
    
    The output is list of PIL images.

2. watermarkList:

    Same like watermarkDir but instead of "dirToSearch" there is "listOfImages" - list of PIL images.
    The output is the same.
    
3. saveImages:

    **input**
        
        - listOfImages: list of PIL images.
        - pathToSave: path to save the watermark images (the folder will be created if not exists).
        

Note that the package supports only jpg\png 

Hope you will enjoy :)
