"""

ULTIMATE hUUTIS KURKKUMOPO
Automated meme generator <3

by: sampozki

"""

from PIL import Image, ImageFont, ImageDraw
from sys import argv


def readimage(imagepath):
    # Reads image and then returns it (really important)
    return Image.open(imagepath)


def addtext(image, text):
    # Adds text to the speakbubble
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('comicneue.ttf', 36)
    draw.text((115, 45), str(text), (0, 0, 0), font=font)
    return image


def addimage(image, subimage):
    # Adds subphoto inside main image
    imagewidth, imageheight = image.size

    subimagewidth, subimageheight = subimage.size
    ratio = subimagewidth / subimageheight

    subimagewidth = int(imagewidth * 0.4)
    subimageheight = int(imagewidth * 0.4 / ratio)

    subimage = subimage.resize((subimagewidth, subimageheight), Image.ANTIALIAS)

    position = imagewidth - subimagewidth, imageheight-subimageheight

    # if image doesn't have alpha layer then except ;)
    try:
        image.paste(subimage, position, subimage)
    except Exception as e:
        print(e)
        image.paste(subimage, position)

    return image


def main():
    # USAGE: subpath = path for subimage, meme = text
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
