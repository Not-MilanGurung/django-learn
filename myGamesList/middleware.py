class JWTAuthCookieMiddleware:
    """
    Transfers access_token from HTTP-only cookie to the Authorization header.
    This lets DRF see the JWT like it would from a normal API client.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        access_token = request.COOKIES.get("access_token")
        if access_token:
            request.META["HTTP_AUTHORIZATION"] = f"Bearer {access_token}"
        return self.get_response(request)