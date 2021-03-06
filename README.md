# Welcome to Watermark Image!


The package will let you watermark batch of images.
This package is written in python 3.5.4

You have 3 methods you can use:

### Installation



You can install the watermark-image from PyPI:

```sh
$ pip install watermarkImage
```

Example usage (You can also see example folder):
    
From code:
      
```sh
>>> from watermarkImage import Logic
>>> from watermarkImage.Position import Position
>>> from PIL import Image
>>>
>>> logo = Image.open(logoPath)
>>> list = Logic.watermarkDir(dirToSearch, logo, Position.TOP_LEFT)
>>> Logic.saveImages(list, pathForNewImages)

```

CMD\ Terminal:
```sh
    $ python watermarkImage\WatermarkLogic.py -dir=[dorWithImages] -logo=[PathToLogo] -opacity=[1-10] -size=[1-4] -position=[1-4]
```

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


License
----

MIT


**Free Software, Hell Yeah!**
