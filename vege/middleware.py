from .models import APILog


class APIMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        app_name = None
        auth_type = None

        if request.resolver_match:
            app_name = request.resolver_match.app_name

        if request.user.is_authenticated:
            auth_type = "Session auth"
        else:
            auth_type = "Anonymous"


        APILog.objects.create(
            auth_type=auth_type,
            app_name=app_name,
            method=request.method,
            endpoint=request.path,
            status_code=response.status_code
            
        )

        return response

        