$(document).ready(function() {
    $("a[id^='lnk']").bind('click', function(event) {
        event.preventDefault();
        var search = location.search;
        var origin = "";
        var dict = {};
        if (search.length > 0) {
            var arr = search.substring(1).split("&");
            
            var arr2;
            var vyraz, key;
            for (index = 0; index < arr.length; ++index) {
                arr2 = arr[index].split("=");
                key = arr2[0];
                vyraz = arr2[1];
                if (key == "sort") {
                    vyraz = vyraz.replace("Plus", "+");
                    vyraz = vyraz.replace("Minus", "-");
                }
                dict[key] = vyraz;
            }
        }
        if ("sort" in dict)
            origin = dict["sort"];
        //id bez lnk
        var id = this.id.substring(3);
        //alert("origin:" + origin + ",new:" + id);
        //return;
        //1.dam do txtsort value, kdyz je tam stejna, zmenim znamenko name+/name-
        //var origin = $("#id_sort").val();
        var newVal;
        if (origin.length > 0 && origin.substring(1) == id) {
            newVal = (origin.substring(0, 1) == "+" ? "-" : "+") + id;
        }
        else {
            newVal = "+" + id;
        }

        var res = newVal.replace("+", "Plus");
        res = res.replace("-", "Minus");
        window.location = "/list/?sort=" + res;
    });
});