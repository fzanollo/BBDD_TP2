var mapFunctionC = function(){
	emit(1, [this.publicacionId, this.importe * this.comision / 100]);
};

var reduceFunctionC = function(key, operaciones){
	comisionMax = 0;
	operacionesConMaxComision = []

	for (var i = 0; i < operaciones.length; i++) {
		if(operaciones[i][1] > comisionMax) comisionMax = operaciones[i][1];
	}

	for (var i = 0; i < operaciones.length; i++) {
		if(operaciones[i][1] == comisionMax) operacionesConMaxComision.push(operaciones[i]);
	}

	return operacionesConMaxComision;
}

db.Ventas.mapReduce( mapFunctionC, reduceFunctionC, {out: "mapReduceC"} )

db.mapReduceC.find()
