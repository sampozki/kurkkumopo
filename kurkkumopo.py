# ULTIMATE hUUTIS KURKKUMOPO
# Automated meme generator <3

# sampozki

# TODO: aivan kaikki

# TODO: Kuvan avaus ja luku
# TODO: Laitettavan kuvan pienennyt
# TODO: Kuvan tallennus
# TODO: PIL kuva in kuv
# TODO: PIL teksti puhekuplaan
# TODO: KOPIOI KOODI FUZUBOTILTA

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
    font = ImageFont.truetype('comic.ttf', 30)
    draw.text((130, 45), str(text), (0, 0, 0), font=font)
    return image


def addimage(image, imagepath):
    # Lisää subkuvan kuvan sisälle oikeaan kohtaan
    pass


def main():
    path = "pohja.png"
    meemi = "PYTHON VITUN MEEMI"
    pohja = readimage(path)
    pohja = addtext(pohja, meemi)

    pohja.save('test.png')


if __name__ == "__main__":
    main()
