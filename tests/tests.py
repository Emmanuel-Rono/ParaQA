from pages.Product_page import Product_Page
def tests():
    
    product = Product_Page()
    product.open_products_page()
    product.verify_products_page_opened()
    assert "Sort" in product.verify_products_page_opened()
    product.get_all_product_elements()
    product.click_a_product()
    product.check_if_product_page_opens()
    product.add_product_to_cart()
    assert "Checkout" in product.check_if_product_was_added_to_cart()
    product.go_to_Cart()
    assert "Shopping Cart" in product.confirm_view_cart_opened()
    assert "Proceed to Checkout" in product.confirm_if_product_is_Available()
    product.checkout()
    assert "Pay Now" in product.Check_if_checkout_if_available()
    
    