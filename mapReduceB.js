var mapFunctionB = function(){
	emit(this.vendedor, this.calificacionVendedor);
	emit(this.comprador, this.calificacionComprador);
};

var reduceFunctionB = function(userId, calificaciones){
	suma = Array.sum(calificaciones);
	promedio = suma / calificaciones.length
	return promedio;
}

db.Ventas.mapReduce( mapFunctionB, reduceFunctionB, {out: "mapReduceB"} )

db.mapReduceB.find()