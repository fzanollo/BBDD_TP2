import json
from random import random, randint, randrange
from pprint import pprint

# LOAD DATA FROM JSON
usuarios_list = json.load(open('usuarios.json'))

# SET OUTPUT FILE
outputFile = open('ventasGenerated', 'w')

# BEGIN WRITING OUTPUT
outputFile.write('[\n')

cantVentasAGenerar = 1000

for i in range(cantVentasAGenerar):

	# VENTA
	venta = '{\n'

	venta += '"publicacionId": "' + str(i + 1) + '",\n'

	#importe
	importe = str(randint(1, 10000)) + '.' + str(randint(0, 99))
	venta += '"importe": ' + str(importe) + ',\n'

	vendedorId = randint(1, 100)
	venta += '"vendedor": {"id": ' + str(usuarios_list[vendedorId-1]['id']) + ', "nombre": "' + str(usuarios_list[vendedorId-1]['name']) + '"}, \n' 

	compradorId = randint(1, 100)
	while vendedorId==compradorId: #para asegurar que no sean iguales
		compradorId = randint(1, 100)
	venta += '"comprador": {"id": ' + str(usuarios_list[compradorId-1]['id']) + ', "nombre": "' + str(usuarios_list[compradorId-1]['name']) + '"}, \n'

	calificacionVendedor = randint(1, 10)
	venta += '"calificacionVendedor": ' + str(calificacionVendedor) + ',\n'

	calificacionComprador = randint(1, 10)
	venta += '"calificacionComprador": ' + str(calificacionComprador) + ',\n'

	comision = 0 if (random() < 0.4) else randrange(0, 100, 10)
	venta += '"comision": ' + str(comision)

	venta += '\n}'

	if (i!=cantVentasAGenerar-1):
		venta += ',\n'

	outputFile.write(venta)

outputFile.write('\n]')