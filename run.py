from flaskwebgui import FlaskUI
from app import app

FlaskUI(app, width=720, height=1280).run()