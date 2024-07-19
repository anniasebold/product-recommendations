from src.views.http_types.http_response import HttpResponse
from .openai_error import OpenAIError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, OpenAIError):
        return HttpResponse(
            status_code=500,
            body={
                "errors": [{
                "title": "OpenAI Error",
                "type": error.error_type,
                "code": error.code,
                "detail": error.message,
            }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
