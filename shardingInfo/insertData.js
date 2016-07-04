var randomDate = function randomDate() {
	var startDate = new Date(2010, 1, 1, 0, 0, 0, 0);
	var endDate = new Date(2014, 12, 31, 0, 0, 0, 0);

	var date = new Date(+startDate + Math.random() * (endDate - startDate));
	var hour = 0 + Math.random() * (11 - 0) | 0;
	date.setHours(hour);
	return date;
}

//-------------------------------------------------------------------------------------------

var publicaciones = [
	{
	"id": 1,
	"titulo": "Hitachi 2 1/2 15 Gauge Angled Finish Nailer With Air Duster",
	"tipoDePublicacion": "productos"
	},
	{
	"id": 2,
	"titulo": "Campbell Hausfeld Pistol Grip Blowgun",
	"tipoDePublicacion": "servicios"
	},
	{
	"id": 3,
	"titulo": "Bostitch 18v Lithium 1/2 Drill/driver Kit And Bonus Drill Bit Set Bundle",
	"tipoDePublicacion": "mixta"
	}
]

var insertData = function(){
	for (var i = 0 ; i < 20000; i++){
		var publicacion = publicaciones[Math.floor(Math.random()*publicaciones.length)];

		publicacion.fecha = randomDate();

		db.publicaciones.insert(publicacion);
	}
}