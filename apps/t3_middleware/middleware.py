from models import HttpRequestStore


class RequestStore(HttpRequestStore):
    def storage(self, request):
        store = HttpRequestStore()
        store.host = request.get_host()
        store.path = request.get_full_path()
        store.method = request.method
        if request.user.is_authenticated():
            store.user = request.user
        store.save()
