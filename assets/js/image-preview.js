///////////////////////////////////////
// Preview image on upload
///////////////////////////////////////
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
    readUploadImgUrl(this);
    $('.uploaded-photo').show();
});