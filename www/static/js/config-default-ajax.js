(function($) {
	$.ajaxSetup({
		statusCode: {
			403: function() {
				var urlLogout = CakePHP.url({
					c: 'acceso',
					a: 'sesion_expirada'
				});
				window.location.replace(urlLogout);
			}
		}
	})
}(jQuery));