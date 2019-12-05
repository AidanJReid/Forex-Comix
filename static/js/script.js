// Initialize materialize elements

function materializeInit() {
            $('.sidenav').sidenav();
            $('.parallax').parallax();
            $('.dropdown-trigger').dropdown();
            $('.collapsible').collapsible();
            $('#modal1').modal();
}
materializeInit();

// Initialize custom elements

$(document).ready(function() {
            $('select').formSelect();
        })