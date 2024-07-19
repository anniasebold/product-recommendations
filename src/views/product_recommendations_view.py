from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.product_recommendations_controller import ProductRecommendationsController

class ProductRecommendationsView:
    """
        Responsibility for interacting with HTTP
    """
    def product_recommendations(self, http_request: HttpRequest) -> HttpResponse:
        controller = ProductRecommendationsController()
        recommendations = controller.get_recommendations()
        return HttpResponse(status_code=200, body=recommendations)
