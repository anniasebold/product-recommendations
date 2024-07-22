import unittest
from unittest.mock import patch
import pandas as pd
from src.controllers.product_recommendations_controller import ProductRecommendationsController

class TestProductRecommendationsController(unittest.TestCase):
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

    def test_initialization(self):
        controller = ProductRecommendationsController()
        self.assertIn('total_sales', controller.products.columns)
        self.assertIn('store_frequency', controller.products.columns)
        self.assertIn('sales_per_store', controller.products.columns)

    def test_create_parameters_columns(self):
        controller = ProductRecommendationsController()
        # total_sales para produto 1
        self.assertEqual(controller.products['total_sales'].iloc[0], 30)
        # store_frequency para produto 1
        self.assertEqual(controller.products['store_frequency'].iloc[0], 1)
        # sales_per_store para loja 101
        self.assertEqual(controller.products['sales_per_store'].iloc[0], 10)

    def test_get_top_products(self):
        controller = ProductRecommendationsController()
        self.assertEqual(len(controller.top_products), 5)

    def test_get_recommendations(self):
        controller = ProductRecommendationsController()
        recommendations = controller.get_recommendations()
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)

    def test_get_recommendations_with_empty_top_products(self):
        empty_df = pd.DataFrame(columns=[
            'product_id',
            'store_id',
            'sales_per_day',
            'product_title',
            'product_price',
            'product_image_url',
            'store_name'
        ])
        patch('pandas.read_csv', return_value=empty_df).start()
        controller = ProductRecommendationsController()
        recommendations = controller.get_recommendations()
        self.assertEqual(recommendations, [])

    def test_file_not_found(self):
        with patch('pandas.read_csv', side_effect=FileNotFoundError("File not found")):
            with self.assertRaises(FileNotFoundError):
                ProductRecommendationsController()

    def test_get_recommendations_format(self):
        controller = ProductRecommendationsController()
        recommendations = controller.get_recommendations()
        self.assertIsInstance(recommendations, list)
        if recommendations:
            self.assertIsInstance(recommendations[0], dict)
