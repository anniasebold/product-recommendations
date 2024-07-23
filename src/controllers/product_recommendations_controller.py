from typing import Dict, List
import pandas as pd
from src.config import Config

class ProductRecommendationsController:
    """
        Responsibility for implementing the product recommendation logic
    """
    def __init__(self, clean_created_columns = True):
        self.products = pd.read_csv(Config.FILE_PATH, sep=',')
        self.clean_created_columns = clean_created_columns
        self.create_parameters_columns()
        self.top_products = self.get_top_products()

    def create_parameters_columns(self):
        """
            Create columns that will be used as parameters for the products DataFrame.
        """
        grouped_by_product_id = self.products.groupby('product_id')
        grouped_by_product_id_store_id = self.products.groupby(['product_id', 'store_id'])

        total_sales = grouped_by_product_id['sales_per_day'].transform('sum')
        store_frequency = grouped_by_product_id_store_id['sales_per_day'].transform('count')
        sales_per_store = grouped_by_product_id_store_id['sales_per_day'].transform('sum')

        self.products['total_sales'] = total_sales
        self.products['store_frequency'] = store_frequency
        self.products['sales_per_store'] = sales_per_store

    def get_top_products(self):
        """
            Returns top 5 products based on sales, store frequency and sales per store.
        """
        grouped_products = self.group_by_product_and_store()
        top_store = self.get_top_store_and_sales(grouped_products)
        top_products = self.select_top_products(top_store)
        if self.clean_created_columns:
            self.clean_up_columns(top_products)
        return top_products

    def group_by_product_and_store(self):
        """
            Groups products by product_id and store_id
        """
        grouped_products = self.products.groupby(['product_id', 'store_id']).agg({
            'total_sales': 'max',
            'store_frequency': 'max',
            'sales_per_store': 'max',
            'product_title': 'first',
            'product_price': 'first',
            'product_image_url': 'first',
            'store_name': 'first'
        }).reset_index()

        return grouped_products

    def get_top_store_and_sales(self, grouped_products):
        """
            Identifies the top store based on frequency that appears and sales per store.
        """
        def get_top_store(group):
            top_store = group.sort_values(
                by=['store_frequency', 'sales_per_store'],
                ascending=[False, False]
            ).iloc[0]
            return top_store

        grouped_products = grouped_products.groupby('product_id')
        top_store_grouped = grouped_products.apply(get_top_store, include_groups=False)
        top_store_grouped= top_store_grouped.reset_index()
        return top_store_grouped

    def select_top_products(self, top_store_grouped):
        """
            Sort products by total sales and selects the top 5.
        """
        top_products = top_store_grouped.sort_values(by=['total_sales'], ascending=False).head(5)
        return top_products

    def clean_up_columns(self, dataframe):
        """
            Cleans up the dataframe dropping unnecessary columns.
        """
        dataframe.drop(columns=['total_sales', 'store_frequency', 'sales_per_store'], inplace=True)

    def get_recommendations(self) -> List[Dict[str, any]]:
        """
            Returns the products recommendations.
        """
        recommendations = self.top_products.to_dict(orient='records')
        return recommendations
