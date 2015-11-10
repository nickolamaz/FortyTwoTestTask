setInterval('get_requests()', 2000)

function get_requests() {
    'use strict';
    $.ajax({
        url: 'requests/getrequests/',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            $('table').html(data.content);
            $('title').html(data.count + ' unviewed requests. 42 Cups Of Coffee');
            console.log(data.count);
        },
        error: function (data) {
            console.log(data);
        }
    });
}