$("#add-comment-form").submit(function(e) {
    let url = $(this).attr('action');
    let data = $(this).serialize();
    var thisForm = $(this);
    $.post(url, data, function(res) {
        console.log(res);
        let newEntry = `<p class="left-align"><span class="italics">${res.username} said</span> (${res.timestamp}): ${res.answer}</p>`;
        // $(".responses p").last().after(newEntry);
        // console.log($(".responses p").last());
        thisForm.parent().children("p").last().append(newEntry);
        document.getElementById("add-comment-form").reset();
    })
    return false;
})
