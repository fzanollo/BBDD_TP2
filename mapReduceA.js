var mapFunctionA = function(){
	emit(this.vendedor, this.importe)
};

var reduceFunctionA = function(userId, importes){
	return Array.sum(importes);
}

db.Ventas.mapReduce( mapFunctionA, reduceFunctionA, {out: "mapReduceA"} )

db.mapReduceA.find()
