(function($) {
	$.fn.hasAttr = function(s) {
		var a = $(this).attr(s);
		return (typeof a !== typeof undefined && a !== false) ? true : false;
	}

	$.fn.outerHTML = function(s) {
		return (s) ? this.before(s).remove() : $("<p/>").append(this.eq(0).clone()).html();
	}
}(jQuery));