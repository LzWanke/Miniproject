from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DontTellAnyone' #Kryptering
from app import routes
