from app import app

from flask import render_template
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import InputRequired
from .pillow import testa
import uuid #Ett bibliotek som ger ett unikt ID

class MemeForm(Form):
    text1 = StringField('Text 1', validators=[InputRequired()]) #Här lagras Text1
    text2 = StringField('Text 2', validators=[InputRequired()]) #Här lagras Text2
    bild = StringField('What picture do you want?', validators=[InputRequired()], render_kw={"placeholder": "1"})   #Här kan man skriva in namnet på bilden man vill göra till en meme


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MemeForm()                                                                   #Visar formen
    if form.validate_on_submit():                                                      #När användaren har skrivit in saker

        sample_out = uuid.uuid4()                                                       #En sträng som generades med hjälp av uuid
        sample_out_html = 'pictures/sample_out/' + str(sample_out) + '.jpg'             #Variablen säger åt meme.html vart den färdiga bilden finns
        # form.title.data
        testa(250, 0, 250, 240, str(sample_out), form.bild.data, form.text1.data, form.text2.data) #Genererar bilden med hjälp av test funktionen i pillow.py

        return render_template('meme.html', sample = sample_out_html)                   #Renderar meme.html där den generade bilden visas
    return render_template('index.html', form=form)
