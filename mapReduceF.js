var mapFunctionF = function(){
	
};

var reduceFunctionF = function(year, facturaciones){
	
}

db.Facturas.mapReduce( mapFunctionF, reduceFunctionF, {out: "mapReduceF"} )

db.mapReduceF.find()
