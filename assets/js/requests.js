///////////////////////////////////////
// Requests block
///////////////////////////////////////
var viewed;

function get_requests() {
    $.ajax({
        url: this.url,
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            $('#requests').html(data.content);
            if (data.count > 0) {
                $('title').html(data.count + ' unviewed requests. 42 Cups Of Coffee');
            } else {
                $('title').html('42 Cups Of Coffee');
            }

            console.log(data.count);
        },
        error: function (data) {
            console.log(data);
        }
    });
}

// If page is viewed sending post request to update data as viewed
function requestsViewed() {
    var csrftoken = $.cookie('csrftoken');
    $.ajax({
        url: this.url,
        type: 'POST',
        dataType: 'json',
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    })
}

// Check window status
$(window).focus(function () {
    viewed = true;
}).blur(function () {
    viewed = false;
});

setInterval(function () {
    if (viewed) {
        requestsViewed();
        viewed = false;
    }
    get_requests();
}, 10000);
