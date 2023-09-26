from rest_framework.views import exception_handler
from common import messages

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.

    response = exception_handler(exc, context)
    
    if response is not None:
        if 'message' in response.data and response.data['message']:
            response.data = {
                            "success" : False,
                            "status_code" : response.status_code,
                            "message" : response.data['message'],
                            "data": None
                            }
        else:
            response.data = {
                            "success" : False,
                            "status_code" : response.status_code,
                            "message" : response.data['detail'],
                            "data": None
                            }

    return response
