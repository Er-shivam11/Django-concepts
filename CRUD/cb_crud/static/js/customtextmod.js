$(document).ready(function () {
    $('.delete-textmod').click(function (e) {
        var pk = $(this).attr('data')
        var view = $(this).attr('view')
        console.log(pk);
        if (!confirm('Do you want to delete ' + view + ' text module')) {
            e.preventDefault();
            console.log("/custom_text_delete/" + pk);
        }
        else {
            $.get("/custom_text_delete/" + pk);
            console.log("/custom_text_delete/" + pk);
            location.reload(true);
        }
        e.preventDefault();

    });
});