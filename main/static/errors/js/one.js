$("#add-exp-form").submit(function(e) {
    let url = $(this).attr('action');
    let data = $(this).serialize();
    $.post(url, data, function(res) {
        if (res.status) {
            let newEntry = `<p class="left-align">${res.username} said: ${res.answer}</p>`;
            $("#add-exp-form").prepend(newEntry);
        }
    })
    return false;
})