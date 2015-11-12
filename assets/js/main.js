function startGetRequests() {
    setInterval('get_requests()', 2000)
};

function get_requests() {
    $.ajax({
        url: 'requests/getrequests/',
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

function readUploadImgUrl(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#image-preview').attr('src', e.target.result);
            console.log(e);
        };

        reader.readAsDataURL(input.files[0]);
    }
}

$('#id_photo').change(function () {
    console.log('it working');
    readUploadImgUrl(this);
});


$('#editForm').ajaxForm({
    beforeSubmit: function (form, options) {
        $("#loading").show();
        $('textarea').attr('disabled', 'disabled');
        $('input').attr('disabled', 'disabled');
        $('.error_field').removeClass();
        $('.text-danger').hide();
    },
    success: function (data) {
        console.log(data)
        $("#success").show();
        setTimeout(function () {
            $("#success").hide();
        }, 5000);
    },
    error: function (resp) {
        $("#error").show();
        var errors = JSON.parse(resp.responseText);
        for (error in errors.errors) {
            var id = '#id_' + error;
            $(id).after('<p class="text-danger text-center">' + errors.errors[error] + '</p>')
        }

        setTimeout(function () {
            $("#error").hide();
        }, 5000);
    },
    complete: function () {
        $('#loading').hide();
        $('textarea').removeAttr('disabled');
        $('input').removeAttr('disabled');
        setTimeout(function () {
            $('.error_field').removeClass();
        }, 5000);

    }
});