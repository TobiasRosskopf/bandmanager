$(document).ready(function () {
    $("#activeSongs, #passivSongs").sortable({
        connectWith: ".connectedSortable"
    }).disableSelection();
});
