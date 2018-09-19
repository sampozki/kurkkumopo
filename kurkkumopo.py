"""

ULTIMATE hUUTIS KURKKUMOPO
Automated meme generator <3

by: sampozki  2018

"""

from PIL import Image, ImageFont, ImageDraw
from sys import argv


# Reads image and then returns it (Separated function is really important;)))) )
def readimage(imagepath):

    return Image.open(imagepath)


# Adds text to the speakbubble
def addtext(image, text):

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('comicneue.ttf', 36)

    draw.text((115, 45), str(text), (0, 0, 0), font=font)

    return image


# Adds subphoto inside main image
def addimage(image, subimage):

    imagewidth, imageheight = image.size

    subimagewidth, subimageheight = subimage.size
    ratio = subimagewidth / subimageheight

    if subimagewidth >= subimageheight:
        subimagewidth = int(imagewidth * 0.4)
        subimageheight = int(imagewidth * 0.4 / ratio)

    else:
        subimageheight = int(imageheight * 0.4)
        subimagewidth = int(imageheight * 0.4 / (1 / ratio))

    subimage = subimage.resize((subimagewidth, subimageheight), Image.ANTIALIAS)

    position = imagewidth - subimagewidth, imageheight-subimageheight

    # if image has an alpha layer then do:
    if subimage.mode in ('RGBA', 'LA'):
        image.paste(subimage, position, subimage)
    else:
        image.paste(subimage, position)

    return image


# USAGE: subpath = path for subimage, meme = text
def main():

    path = "pohja.png"
    print(argv)
    if len(argv) == 3:
        meme = argv[1]
        subpath = argv[2]
    else:
        subpath = "top.png"
        meme = ""
        if meme == "":
            meme = "KURKKU VITUN MOPO :D"

    bottomimage = readimage(path)
    subimage = readimage(subpath)
    bottomimage = addtext(bottomimage, meme)
    addimage(bottomimage, subimage)

    bottomimage.save('test.png')


if __name__ == "__main__":
    main()
