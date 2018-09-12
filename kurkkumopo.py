# ULTIMATE hUUTIS KURKKUMOPO
# Automated meme generator <3

# sampozki

# TODO: aivan kaikki

# TODO: Kuvan avaus ja luku DONE
# TODO: Laitettavan kuvan pienennyt
# TODO: Kuvan tallennus DONE
# TODO: PIL kuva in kuv DONE
# TODO: PIL teksti puhekuplaan DONE
# TODO: KOPIOI KOODI FUZUBOTILTA DONE

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def readimage(imagepath):
    # Lukee kuvan tiedostosta ja palauttaa sen
    kuva = Image.open(imagepath)
    return kuva


def addtext(image, text):
    # Lisää kuvan puhekuplaan tekstiä ja palauttaa kuvan
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('comicneue.ttf', 32)
    draw.text((115, 45), str(text), (0, 0, 0), font=font)
    return image


def addimage(image, subimage):
    # Lisää subkuvan kuvan sisälle oikeaan kohtaan
    imagewidth, imageheight = image.size
    subimagewidth, subimageheight = subimage.size

    # TODO: resize subimage sopivan kokoiseksi

    position = imagewidth-subimagewidth, imageheight-subimageheight
    image.paste(subimage, position, subimage)

    return image


def main():
    # USAGE: vaihda subpath kuvaan ja sitten meemiin jotain jos haluu :DDDDD
    path = "pohja.png"
    subpath = "top.png"
    meemi = "KURKKU VITUN MOPO :D"
    pohja = readimage(path)
    subimage = readimage(subpath)
    pohja = addtext(pohja, meemi)
    addimage(pohja, subimage)

    pohja.save('test.png')


if __name__ == "__main__":
    main()
