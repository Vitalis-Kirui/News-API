from flask import Flask
from app.config import DevConfig

#Initializing the application
app = Flask(__name__)

#Setting up configurations
app.config.from_object(DevConfig)

from app import views