from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.product_recommendations_controller import ProductRecommendationsController

class ProductRecommendationsView:
    """
        Responsibility for interacting with HTTP
    """
    def product_recommendations(self, http_request: HttpRequest) -> HttpResponse:
        controller = ProductRecommendationsController()
        user_id = http_request.query_params.get("user_id")
        recommendations = controller.get_recommendations()

        response_body = {
            "user_id": user_id,
            "recommendations": recommendations
        }

        return HttpResponse(status_code=200, body=response_body)
