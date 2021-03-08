'use strict';

(function($) {
    $(function() {
        var iniSearchForm = $("#initial-search-form");
        var doSearch = $(".do-search");

        iniSearchForm.submit(function(e, follow) {

            if (typeof follow === "undefined") {
                e.preventDefault();
            }
        });

        doSearch.click(function() {
            iniSearchForm.trigger('submit', [true]);
        });

        $("#feeling-lucky").click(function() {
            iniSearchForm.append($("<input type='hidden' name='lucky'/>"));
            iniSearchForm.trigger('submit', [true]);
        });
    });
})($);