$(document).ready(function () {

    // Connect sortable songlists
    $("#activeSongs, #passivSongs").sortable({
        connectWith: ".connectedSortable"
    }).disableSelection();

});
