from models import HttpRequestStore


class RequestStore(object):
    def process_request(self, request):
        if not request.is_ajax():
            HttpRequestStore(
                host=request.get_host(),
                path=request.get_full_path(),
                method=request.method
                ).save()
        return None
