from django.forms import FileInput


class PreviewImage(FileInput):
    class Media:
        js = (
            'js/jquery-1.11.3.min.js',
            'js/image-preview.js'
        )
        css = {
            'all': ('css/main.css',)
        }
