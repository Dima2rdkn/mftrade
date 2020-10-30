$(document).ready(function() {
    $('.add-item').click(function(ev) {
        ev.preventDefault();
        var count = $('#items-form-container').children().length;
        var tmplMarkup = $('#item-template').html();
        var compiledTmpl = tmplMarkup.replace(/__prefix__/g, count);
        $('div#items-form-container').append(compiledTmpl);
        //       $('#item-1').clone(true).unwrap().appendTo('#items-form-container');
        // update form count
        $('#id_item_items-TOTAL_FORMS').attr('value', count+1);

        // some animate to scroll to view our new form
        $('html, body').animate({
                scrollTop: $("#add-item-button").position().top-200
            }, 800);
    });
});