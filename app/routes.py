import sys
import os.path
from flask import Flask,Response
from resource.holiday import HolidayResource

sys.path.append(os.path.abspath('./resource'))
sys.path.append(os.path.abspath('./domain'))
sys.path.append(os.path.abspath('./util'))

app = Flask(__name__)

@app.route("/")
def index():
	return Response({ 'app_name': "Pasco", 'app_description': 'Pasco: all the holidays.' }, mimetype='application/json')

@app.route("/<int:year>/holidays")
def holidays(year):
	return Response(HolidayResource().list(year), mimetype='application/json')

if __name__ == "__main__":
	app.run()
