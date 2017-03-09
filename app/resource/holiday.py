from domain.holiday import Holiday
from util.holiday import easter_sunday,dt_converter
from datetime import datetime, timedelta
import json

class HolidayResource(object):

	def list(self, year):
		lista = []
		es = easter_sunday(year)

		''' carnaval '''
		dt = es - timedelta(days=47)
		lista.append(Holiday(dt, "Carnaval", False))

		''' quarta de cinzas '''
		dt = es - timedelta(days=46)
		lista.append(Holiday(dt, "Quarta-feira de Cinzas", False))

		''' paixao '''
		dt = es - timedelta(days=2)
		lista.append(Holiday(dt, "Sexta-feira da Paixao", False))

		''' pascoa '''
		lista.append(Holiday(es, "Pascoa", False))

		''' corpus christi '''
		dt = es + timedelta(days=60)
		lista.append(Holiday(dt, "Corpus Christi", False))

		return json.dumps([obj.__dict__ for obj in lista], default = dt_converter)
