from datetime import datetime
from util.holiday import dt_converter
import json

class Holiday(object):
	def __init__(self, date, name, is_fixed):
		self.date = date
		self.name = name
		self.is_fixed = is_fixed

	def __str__(self):
		return name + ' - ' + date.strftime('%d/%m/%Y')

	def to_json(self):
		return json.dumps(self.__dict__, default=dt_converter)