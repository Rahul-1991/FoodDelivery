from django.http import JsonResponse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from jsonschema import FormatChecker, ValidationError, validate
from functools import wraps


def render_response_json(stat, message, data):
    return JsonResponse(data={'s': stat, 'm': message, 'd': data}, status=HTTP_200_OK)


def render_error_response(message):
    return JsonResponse(data={'s': 0, 'm': message, 'd': {}}, status=HTTP_400_BAD_REQUEST)


def process_params(param_config=None):
    def deco(f):

        def extract_params(request):
            if request.method == 'POST':
                return request.get_json()
            else:
                return request.GET

        @wraps(f)
        def decorated_function(cls, request, *args, **kwargs):
            params = extract_params(request)
            print params, param_config
            try:
                validate(params, param_config, format_checker=FormatChecker())
                return f(cls, request, params=params, *args, **kwargs)
            except Exception as e:
                print e
                return render_error_response(e.message)
        return decorated_function
    return deco
