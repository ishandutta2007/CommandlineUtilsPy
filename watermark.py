import os
import sys
from PIL import Image

if len(sys.argv) < 4:
    print('Usage: watermark.py \'input image folder path\'  \'output image folder path\'  \'logo path\' [topleft, topright, bottomleft, bottomright, center]')
    sys.exit()
elif len(sys.argv) == 5:
    path = sys.argv[1]
    opath = sys.argv[2]
    lgo = sys.argv[3]
    pos = sys.argv[4]
else:
    path = sys.argv[1]
    opath = sys.argv[2]
    lgo = sys.argv[3]

logo = Image.open(lgo)
logoWidth = logo.width
logoHeight = logo.height
print(logoWidth)
print(logoHeight)

for filename in os.listdir(path):
    if (filename.endswith('.jpg') or filename.endswith('.png')) and (filename != lgo):
        image = Image.open(path + '/' + filename)
        imageWidth = image.width
        imageHeight = image.height
        print(imageWidth)
        print(imageHeight)
        if logoHeight*10>imageHeight:
            newlogoHeight = int(imageHeight/10)
            newlogoWidth = int(logoWidth*newlogoHeight/logoHeight)
            print(newlogoWidth)
            print(newlogoHeight)
            size = newlogoWidth, newlogoHeight
            logo.thumbnail(size, Image.ANTIALIAS)
        try:
            if pos == 'topleft':
                image.paste(logo, (0, 0), logo)
            elif pos == 'topright':
                image.paste(logo, (imageWidth - newlogoWidth, 0), logo)
            elif pos == 'bottomleft':
                image.paste(logo, (0, imageHeight - newlogoHeight), logo)
            elif pos == 'bottomright':
                image.paste(logo, (imageWidth - newlogoWidth, imageHeight - newlogoHeight), logo)
            elif pos == 'center':
                image.paste(logo, ((imageWidth - newlogoWidth)/2, (imageHeight - newlogoHeight)/2), logo)
            else:
                print('Error: ' + pos + ' is not a valid position')
                print('Usage: watermark.py \'input folder path\' \'output folder path\' \'logo path\' [topleft, topright, bottomleft, bottomright, center]')

            image.save(opath + '/' + filename)
            print('Added watermark to ' + opath + '/' + filename)

        except:
            image.paste(logo, ((imageWidth - newlogoWidth)/2, (imageHeight - newlogoHeight)/2), logo)
            image.save(path + '/' + filename)
            print('Added default watermark to ' + path + '/' + filename)



