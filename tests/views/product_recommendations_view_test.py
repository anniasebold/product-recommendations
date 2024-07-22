import unittest
from unittest.mock import patch
import pandas as pd
from src.controllers.product_recommendations_controller import ProductRecommendationsController
from src.views.product_recommendations_view import ProductRecommendationsView
from src.views.http_types.http_request import HttpRequest

class TestProductRecommendationsView(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'product_id': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
            'store_id': [101, 102, 101, 103, 102, 103, 104, 105, 106, 107],
            'sales_per_day': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
            'product_title': ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E'],
            'product_price': [100, 100, 150, 150, 200, 200, 250, 250, 300, 300],
            'product_image_url': [
                'url1',
                'url1',
                'url2',
                'url2',
                'url3',
                'url3',
                'url4',
                'url4',
                'url5',
                'url5'
            ],
            'store_name': [
                'Store1',
                'Store2',
                'Store1',
                'Store3',
                'Store2',
                'Store3',
                'Store4',
                'Store5',
                'Store6',
                'Store7'
            ]
        })
        patch('src.config.Config.FILE_PATH', 'fake_path').start()
        patch('pandas.read_csv', return_value=self.df).start()

    def tearDown(self):
        patch.stopall()

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
