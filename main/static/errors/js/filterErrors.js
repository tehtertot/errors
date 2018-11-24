$("#lang-filter").change(function() {
    var languageId = $("#lang-filter").val();
    $.get(`/filter/${languageId}`, function(res) {
        $("#error-list").html(res);
    })
})