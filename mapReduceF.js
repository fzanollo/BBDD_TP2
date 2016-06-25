var mapFunctionF = function(){
	emit(this.tipoDePublicacion, this.id);
};

var reduceFunctionF = function(tipoDePublicacion, publicaciones){
	return publicaciones.length;
}

db.Publicaciones.mapReduce( mapFunctionF, reduceFunctionF, {out: "mapReduceF"} )

db.mapReduceF.find()