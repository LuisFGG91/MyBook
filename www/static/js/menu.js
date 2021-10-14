(function($, document) {
    var menuPrincipal = null,
        opcionMarcada = null;

    var init = function() {
        menuPrincipal = $('[data-model="menu-principal"]');
    }

    var buscaLink = function() {
        $.each(menuPrincipal.find('a'), function(index, a) {
            var link = $(a);
            if (verificaLink(link.attr('href'), index)) {
                opcionMarcada = link;
                activaOpcion();
                return false;
            }
        });

        if (opcionMarcada === null) {
            var link = $(menuPrincipal.find('a').get(0));
            if (verificaLink(link.attr('href'), null)) {
                opcionMarcada = link;
                activaOpcion();
            }
        }
    }

    var verificaLink = function(href, indexExcluir) {
        locationHref = window.location.href;
        n = locationHref.search(href);
        if (indexExcluir !== 0) {
            if (n == 0) {
                return true;
            }
        }
        return false;
    }

    var activaOpcion = function() {
        opcionMarcada.parents('li').addClass('active');
        opcionMarcada.parents('ul.collapse').addClass('in').attr('aria-expanded', true);
    }

    $(document).ready(function() {
        init();
        buscaLink();
    });
}(jQuery, document));