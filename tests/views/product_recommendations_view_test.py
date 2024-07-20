import unittest
from unittest.mock import patch
from src.controllers.product_recommendations_controller import ProductRecommendationsController
from src.views.product_recommendations_view import ProductRecommendationsView
from src.views.http_types.http_request import HttpRequest

class TestProductRecommendationsView(unittest.TestCase):
    def test_product_recommendations(self):
        view = ProductRecommendationsView()
        http_request = HttpRequest(query_params={'user_id': '123'})

        with patch.object(ProductRecommendationsController, 'get_recommendations',
                          return_value=[{'product_id': 1, 'product_title': 'Test Product'}]):
            response = view.product_recommendations(http_request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.body['user_id'], '123')
        self.assertEqual(
            response.body['recommendations'],
            [
                {
                    'product_id': 1,
                    'product_title': 'Test Product'
                }
            ])
