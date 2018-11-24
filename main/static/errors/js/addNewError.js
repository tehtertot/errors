$("#add-error-form").submit(function() {
    let url = $(this).attr('action');
    let data = new FormData($(this).get(0));

    // for (var pair of data.entries()) {
    //     console.log(pair[0]+ ', ' + pair[1]); 
    // }
    
    if (errorImage && codeErrorImage) {
        data.append("error", errorImage);
        data.append("code-error", codeErrorImage);
        if (codeFixImage) {
            data.append("code-fix", codeFixImage);
        }
        $.ajax({
            url: url,
            type: "POST",
            data: data,
            dataType: 'json',
            cache: false,
            contentType: false,
            processData: false,
            success: function(res) {
                document.getElementById('add-error-form').reset();
                $("#add-error").text("");
                errorImage = null;
                codeErrorImage = null;
                codeFixImage = null;
                pastedImageFile = null;
            
                var instance = M.Modal.getInstance($("#submit-images-modal"));
                instance.close();
                slideIndex = res.size;
                if (slideIndex == 1) {
                    // first set of images
                    $(".w3-display-container").append(res.html);
                } else {
                    // add to the end
                    $(".individual-slides").last().after(res.html);
                    if (slideIndex == 2) {
                        // add slide buttons
                        $(".w3-display-container").last().after(`<button class="w3-button w3-display-left" onclick="plusDivs(-1)">&#10094;</button>
                        <button class="w3-button w3-display-right" onclick="plusDivs(+1)">&#10095;</button>`)
                    }
                }
                showDivs(slideIndex);
            },
            error: function(err) {
                console.log(err);
            }
        });
    }
    else {
        $("#add-error").text("Please provide images of both the error and your code");
    }
    return false;
})

$("#update-form").submit(function(e) {
    let url = $(this).attr('action');
    let data = new FormData($(this).get(0));
    
    var parentDiv = $(this).parent();

    if (codeFixImage) {
        data.append("code-fix", codeFixImage);
        
        $.ajax({
            url: url,
            type: "POST",
            data: data,
            dataType: 'json',
            cache: false,
            contentType: false,
            processData: false,
            success: function(res) {
                codeFixImage = null;
                pastedImageFile = null;
            
                let newDivContent = `<p>Code After</p><img src="/${res.imageURL}" alt="error">`
                parentDiv.html(newDivContent);
            },
            error: function(err) {
                console.log(err);
            }
        });
    }
    return false;
})