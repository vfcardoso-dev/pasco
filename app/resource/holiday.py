from domain.holiday import Holiday
from util.holiday import easter_sunday,dt_converter
from datetime import datetime, timedelta
import json

class HolidayResource(object):

	def list(self, year):
		pascoa = easter_sunday(year) # Recupera domingo de pascoa
		carnaval = pascoa - timedelta(days=47) # Carnaval
		cinzas = pascoa - timedelta(days=46)  # Cinzas
		paixao = pascoa - timedelta(days=2) # Paixao
		corpus_christi = pascoa + timedelta(days=60) # Corpus Christi
		
		lista = []
		lista.append(Holiday(datetime(year, 1, 1), "Ano novo", True))
		lista.append(Holiday(carnaval, "Carnaval", False))
		lista.append(Holiday(cinzas, "Quarta-feira de Cinzas", False))
		lista.append(Holiday(paixao, "Sexta-feira da Paixao", False))
		lista.append(Holiday(pascoa, "Pascoa", False))
		lista.append(Holiday(datetime(year, 4, 21), "Tiradentes", True))
		lista.append(Holiday(datetime(year, 5, 1), "Dia do Trabalho", True))
		lista.append(Holiday(corpus_christi, "Corpus Christi", False))
		lista.append(Holiday(datetime(year, 9, 7), "Independencia do Brasil", True))
		lista.append(Holiday(datetime(year, 10, 12), "Nossa Senhora Aparecida", True))
		lista.append(Holiday(datetime(year, 11, 2), "Finados", True))
		lista.append(Holiday(datetime(year, 11, 15), "Proclamacao da Republica", True))
		lista.append(Holiday(datetime(year, 12, 25), "Natal", True))

		sorted(lista, key=lambda hl: hl.date)

		return json.dumps([obj.__dict__ for obj in lista], default = dt_converter)
