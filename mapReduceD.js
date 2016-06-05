var mapFunctionD = function(){
	facturaciones = new Array();

	if(this.hasOwnProperty('abonoFijo')){
		var abono = this.abonoFijo.abono;
		facturaciones.push(abono);
	}

	if(this.hasOwnProperty('comisiones')){
		var comisiones = this.comisiones;

		for (var i = 0; i < comisiones.length; i++) {
			facturaciones.push(comisiones[i].comision)
		}
	}

	emit(this.fecha.slice(this.fecha.length-2, this.fecha.length), facturaciones)
};

var reduceFunctionD = function(year, facturaciones){
	
	facturacionesFlattened = facturaciones.reduce(function(a, b){return a.concat(b)}, []);

	facturacionAnual = Array.sum(facturacionesFlattened);

	return facturacionAnual;
}

db.Facturas.mapReduce( mapFunctionD, reduceFunctionD, {out: "mapReduceD"} )

db.mapReduceD.find()
