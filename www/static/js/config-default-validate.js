(function($) {
	if(!$.fn.validate) return;

	$.validator.setDefaults({
		ignore: ':disabled,:hidden:not(.chosen)',
		errorPlacement: function(error, element) {},
		highlight: function(element, errorClass, validClass) {
			if (!$(element).is('input[type="checkbox"]')) {
				$(element).parents('.form-group').addClass('has-error');
			}
		},
		unhighlight: function(element, errorClass, validClass) {
			if (!$(element).is('input[type="checkbox"]')) {
				$(element).parents('.form-group').removeClass('has-error');
			}
		}
	});
}(jQuery));