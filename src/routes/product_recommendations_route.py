from flask import Blueprint, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.product_recommendations_view import ProductRecommendationsView
from src.errors.error_handler import handle_errors

product_recommendations_bp = Blueprint('product_recommendations', __name__,
                                        url_prefix='/product-recommendations')

@product_recommendations_bp.route('/<int:user_id>', methods=["GET"])
def product_recommendations(user_id):
    response = None
    try:
        product_recommendations_view = ProductRecommendationsView()
        http_request = HttpRequest(query_params={"user_id": user_id})
        response = product_recommendations_view.product_recommendations(http_request)
    except Exception as exception:
        response = handle_errors(exception)

    return jsonify(response.body), response.status_code
