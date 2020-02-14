#Do I need any database stuff? Or can I go straight from
#forms to a calculation, and print the result?
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from roipage import routes