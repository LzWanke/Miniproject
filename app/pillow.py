from app import app
from PIL import Image, ImageDraw, ImageFont
import os
# get an image

basedir = os.path.abspath(os.path.dirname(__file__))
app.logger.debug('basedir: %s', basedir)


def testa(width_t1, height_t1, width_t2, height_t2, sample_out, sample_in, text1, text2):
    infile = os.path.join(basedir, 'static/pictures/sample_in/' + sample_in + '.jpg')   #Tar en bild som finns i sample_in mappen
    outfile = os.path.join(basedir, 'static/pictures/sample_out/' + sample_out + '.jpg')#Här ska den sparade bilden hamna
    fontfile = os.path.join(basedir, 'font/Raleway-Regular.ttf')    #Fonten på bilden

    base = Image.open(infile).convert('RGBA')   #Variabel på bilden



    fnt_size = (20)
    # Gör en ny bild för att texten ska fungera bra
    txt = Image.new('RGBA', base.size, (255,255,255,0))

    # fonten jag vll ha
    fnt = ImageFont.truetype(fontfile, 100)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # Text 1
    d.text((width_t1, height_t1), text1, font=fnt, fill=(0,0,0,255))
    # Text 2
    d.text((width_t2, height_t2), text2, font=fnt, fill=(0,0,0,255))

    out = Image.alpha_composite(base, txt).convert('RGB')

    out.save(outfile) #Spara bilden
