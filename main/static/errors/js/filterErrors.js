$("#frm-filter").change(function() {
    console.log($("#frm-filter").val())
    $.get(`/filter/${$("#frm-filter").val()}`, function(res) {
        $("#error-list").html(res);
    })
})