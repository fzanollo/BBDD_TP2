import json
from random import random, randint, randrange
from pprint import pprint

# TIPOS DE PUBLICACION
tiposDePublicacion = ['"servicios"', '"productos"', '"mixta"']

# LOAD DATA FROM JSON
titulos_list = json.load(open('titulos.json'))

# SET OUTPUT FILE
outputFile = open('publicacionesGenerated', 'w')

# BEGIN WRITING OUTPUT
outputFile.write('[\n')

cantPublicacionesAGenerar = 1000

for i in range(cantPublicacionesAGenerar):

	# VENTA
	publicacion = '{\n'

	#id
	pId = i+1
	publicacion += '"id": ' + str(pId) + ',\n'

	titulo = '"' + str(titulos_list.pop()['titulo']) + '"'
	publicacion += '"titulo": ' + titulo + ',\n'

	tipoDePublicacion = tiposDePublicacion[randint(0, 2)]
	publicacion += '"tipoDePublicacion": ' + tipoDePublicacion

	publicacion += '\n}'

	if (i!=cantPublicacionesAGenerar-1):
		publicacion += ',\n'

	outputFile.write(publicacion)

outputFile.write('\n]')