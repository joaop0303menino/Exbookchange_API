from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data = {
            "status": response.status_code,
            "error": getattr(exc, "default_code", "error"),
            "message": str(getattr(exc, "detail", exc))
        }

    else:
        import traceback
        response = {
            "status": 500,
            "error": "internal_error",
            "message": str(exc),
            "trace": traceback.format_exc()
        }
        from rest_framework.response import Response
        from rest_framework import status
        response = Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
