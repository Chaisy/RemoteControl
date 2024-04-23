from django.utils.deprecation import MiddlewareMixin

class DisableCsrfForNgrokMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.get_host().endswith('.ngrok.io'):
            setattr(request, '_dont_enforce_csrf_checks', True)
