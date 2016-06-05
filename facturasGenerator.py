import json
from random import randint
from datetime import date
from pprint import pprint

def addInterval(fecha):
	newMonth = fecha.month + 12
	if newMonth>12:
		return date(fecha.year +1, 1, fecha.day)
	else:
		return date(fecha.year, newMonth, fecha.day)

# LOAD DATA FROM JSON
titulos_list = json.load(open('titulos.json'))
usuarios_list = json.load(open('usuarios.json'))

# SET INITIAL DATE
fecha = date(1990, 1, 1)

# SET OUTPUT FILE
outputFile = open('facturasGenerated', 'w')

# BEGIN WRITING OUTPUT
outputFile.write('[\n')

intervalQuantity = 6;

for months in range(intervalQuantity):
		
	#------------ BEGIN MONTH
	for iuser in range(len(usuarios_list)):
		factura = '{\n'

		#usuario
		factura += '"usuario": {"id": ' + str(usuarios_list[iuser]['id']) + ', "nombre": "' + str(usuarios_list[iuser]['name']) + '"}, \n' 

		#fecha
		factura += '"fecha": "' + fecha.strftime("%d/%m/%y") + '"'

		#abono fijo
		cantAbonoFijo = randint(0, 3)

		if cantAbonoFijo>0:
			factura += ',\n"abonoFijo": { "publicaciones": ['

			for i in range(0, cantAbonoFijo):
				factura += '"' + str(titulos_list.pop()['titulo']) + '"'
				if i!=cantAbonoFijo-1:
					factura += ', '

			factura += '], "abono": 300 }'

		#comisiones
		cantComision = randint(0, 4)

		if cantComision>0:
			factura += ',\n"comisiones": ['

			for i in range(0, cantComision):
				comision = str(randint(1, 100)) + '.' + str(randint(0, 99)) 

				factura += '{ "titulo": "' + str(titulos_list.pop()['titulo']) + '", "comision": ' + comision + '}'

				if i!=cantComision-1:
					factura += ', '

			factura += ']'

		factura += '\n}'

		outputFile.write(factura)

		if not(iuser==len(usuarios_list)-1 and months==intervalQuantity-1) :
			outputFile.write(',\n')
	#---------- END MONTH

	fecha = addInterval(fecha);

# FINISH WRITING OUTPUT


outputFile.write('\n]')