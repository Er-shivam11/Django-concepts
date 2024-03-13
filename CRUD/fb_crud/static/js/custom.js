$(document).ready(function () {
    $(".menus button").on("click", function () {
        $("#content").addClass("full-width");
        $("#content_body").hide();
        $("#show_sidebar").show();
    });
    $("#show_sidebar").on("click", function () {
        $("#content").removeClass("full-width");
        $("#content_body").show();
        $("#show_sidebar").hide();
    });


    setInterval(async function () {
        await refresh_printing_status();
    }, 1000);

    async function refresh_printing_status() {
        await $('#reload-content').load(" #reload-content>*", "" + "");
    }
});




function filterResult(){
    var filter = document.getElementById("filter-select").value;
    var rows = document.getElementsByClassName("row-filter");
    for (var i = 0; i < rows.length; i++)
    {
        var row = rows[i];
        var isVerified = row.getAttribute("data-verified")
        if (filter === "all" || filter === "isVerified")
        {
            row.style.display = "table-row";
        }
            
    
        else
        {
            row.style.display="none"
        }
    }
        

}





