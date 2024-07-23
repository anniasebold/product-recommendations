from typing import List
import os
import sys
import matplotlib.pyplot as plt
from src.controllers.product_recommendations_controller import ProductRecommendationsController

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def generate_sales_by_product_chart(products: List[str], column, label, name):
    plt.figure(figsize=(20, 10))
    plt.bar(products, column, color='blue')

    plt.title(f'{name} por Produto')
    plt.xlabel('Produtos')
    plt.ylabel(name)

    output_dir = 'visualizations'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    plt.savefig(os.path.join(output_dir, f'{label}_by_product.png'))
    plt.show()

if __name__ == "__main__":
    controller = ProductRecommendationsController(clean_created_columns=False)

    recommendations = controller.get_recommendations()

    product_titles = [rec['product_title'] for rec in recommendations]
    total_sales = [rec['total_sales'] for rec in recommendations]
    store_frequency = [rec['store_frequency'] for rec in recommendations]
    sales_per_store = [rec['sales_per_store'] for rec in recommendations]

    generate_sales_by_product_chart(product_titles, total_sales, 'total_sales', 'Total de Vendas')
    generate_sales_by_product_chart(
        product_titles,
        store_frequency,
        'store_frequency',
        'Frequência de Lojas'
      )
    generate_sales_by_product_chart(
        product_titles,
        sales_per_store,
        'sales_per_store',
        'Vendas por Loja'
      )
