class ExampleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.META['HTTP_ACCEPT_ENCODING'] = "UTF-8"
        response = self.get_response(request)
        return response
