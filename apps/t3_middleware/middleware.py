from t1_base.models import HttpRequestStore

class HttpRequestStore:
    def storage(self, request):
        store = HttpRequestStore()
        store.host = request.get_host()
        store.path = request.get_full_path()
        store.method = request.method
        if request.user.is_authenticated():
            store.user = request.user
        store.save()