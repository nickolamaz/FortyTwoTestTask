from models import HttpRequestStore


class RequestStore(object):
    def process_request(self, request):
        if not request.is_ajax():
            store = HttpRequestStore()
            store.host = request.get_host()
            store.path = request.get_full_path()
            store.method = request.method
            store.save()
        return None
