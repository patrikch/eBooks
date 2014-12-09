$(document).ready(function() {
    $("a[id^='lnk']").bind('click', function(event) {
        event.preventDefault();
        //id bez lnk
        var id = this.id.substring(3);
        //1.dam do txtsort value, kdyz je tam stejna, zmenim znamenko name+/name-
        var origin = $("#id_sort").val();
        if (origin.length > 0 && origin.substring(1) == id) {
            $("#id_sort").val((origin.substring(0, 1) == "+" ? "-" : "+") + id);
        }
        else {
            $("#id_sort").val("+" + id);
        }
        //2.odeslu formular 
        $("#btnSearch").click();
    });
});