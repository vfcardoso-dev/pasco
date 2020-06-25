import sys
import os.path
import json
from flask import Flask,Response
from resource.holiday import HolidayResource

sys.path.append(os.path.abspath('./resource'))
sys.path.append(os.path.abspath('./domain'))
sys.path.append(os.path.abspath('./util'))

app = Flask(__name__)

@app.route("/")
def index():
	d = { 
		"app_name": "Pasco", 
		"app_description": "Pasco: all the holidays.",
		"app_repository": "https://github.com/vfcardoso-dev/pasco",
		"app_instructions": "List all brazilian holidays from a given year: /:year:/holidays"
	}
	return Response(json.dumps(d, indent=2), mimetype='application/json')

@app.route("/<int:year>/holidays")
def holidays(year):
	return Response(HolidayResource().list(year), mimetype='application/json')

if __name__ == "__main__":
    app.run(threaded=True)
