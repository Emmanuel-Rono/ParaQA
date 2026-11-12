from pages.Product_page import Product_Page
def tests():
    
    product = Product_Page()
    product.open_products_page()
    product.verify_products_page_opened()
    assert "Sort" in product.verify_products_page_opened()