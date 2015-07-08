$(document).on("ready" , der);
	function der()
	{
		var cambioCSS =
		{
			width: "100%",
			color: "#F00",
			height: "auto"
		};
		$("#video").css(cambioCSS);
	}

	function cambio()
	{
		$('section').hide('1000000').show('slow');
	}
