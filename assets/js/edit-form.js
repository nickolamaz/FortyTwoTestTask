///////////////////////////////////////
// Edit form handling
///////////////////////////////////////
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
        if ($('#id_photo').val()) {
            window.location.reload()
        }

    }
});