from models import HttpRequestStore


class RequestStore(object):
    def process_request(self, request):
        store = HttpRequestStore()
        store.host = request.get_host()
        store.path = request.get_full_path()
        store.method = request.method
        if request.user.is_authenticated():
            store.user = request.user
        # store.save()
        return None
