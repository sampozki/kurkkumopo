"""

ULTIMATE hUUTIS KURKKUMOPO
Automated meme generator <3

by: sampozki

"""

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from sys import argv


def readimage(imagepath):
    # Lukee kuvan tiedostosta ja palauttaa sen
    kuva = Image.open(imagepath)
    return kuva


def addtext(image, text):
    # Lisää kuvan puhekuplaan tekstiä ja palauttaa kuvan
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('comicneue.ttf', 36)
    draw.text((115, 45), str(text), (0, 0, 0), font=font)
    return image


def addimage(image, subimage):
    # Lisää subkuvan kuvan sisälle oikeaan kohtaan
    imagewidth, imageheight = image.size

    subimagewidth, subimageheight = subimage.size
    suhde = subimagewidth / subimageheight
    subimagewidth = int(imagewidth * 0.4)
    subimageheight = int(imagewidth * 0.4 / suhde)

    subimage = subimage.resize((subimagewidth, subimageheight), Image.ANTIALIAS)

    position = imagewidth - subimagewidth, imageheight-subimageheight
    try:
        image.paste(subimage, position, subimage)
    except Exception as e:
        print(e)
        image.paste(subimage, position)

    return image


def main():
    # USAGE: vaihda subpath kuvaan ja sitten meemiin jotain jos haluu :DDDDD
    path = "pohja.png"
    print(argv)
    if len(argv) == 3:
        meemi = argv[1]
        subpath = argv[2]
    else:
        subpath = "top.png"
        meemi = ""
        if meemi == "":
            meemi = "KURKKU VITUN MOPO :D"
    pohja = readimage(path)
    subimage = readimage(subpath)
    pohja = addtext(pohja, meemi)
    addimage(pohja, subimage)

    pohja.save('test.png')


if __name__ == "__main__":
    main()
