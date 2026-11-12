
import os
# Before
from helium import go_to, start_chrome, write, click, Text, S, find_all, wait_until, kill_browser
class Product_Page:
    def __init__(self):
        self.url = "https://demo.spreecommerce.org/us/en/products"
    
    #1.Open Products page
    def open_products_page(self):
        start_chrome(self.url)
        
    # Verify that page is open
    def verify_products_page_opened(self):
        message_locator= Text("Sort")
        wait_until(message_locator.exists, timeout_secs=10)
        actual_text =  message_locator. web_element.text
        return actual_text
    #2.Verify that sort is available
    
    #2.Click a product
    
    # Get all product links
    PRODUCT_LINK_SELECTOR = ".group a[href*='/products/']"
    
    def get_all_product_elements(self):
        links = find_all(S(self.PRODUCT_LINK_SELECTOR))
        if not links:
            raise RuntimeError(f"No products found")
        return links
         
    def click_a_product(self):
        product_links = self.get_all_product_elements()
        click(product_links[0])
        wait_until(Text("ADD TO CART").exists, timeout_secs=10)
    
    #Check that product details are displayed
    #3.Add to cart
    
    def add_product_to_cart():
        click("add to cart")
        wait_until(Text("View Cart").exists, timeout_secs=10)
    #5.Check if cart appears as slideing windowres
    def check_if_slide_window():
        message_locator = Text("Chekout")
        wait_until(message_locator.exists, timeout_secs= 10)
        actual_text = message_locator.web_element.text
        return actual_text
    #6.View Cart
    def view_cart():
        message_locator = Text("Cart")
        wait_until(message_locator.exists, timeout_secs= 10)
        actual_text = message_locator.web_element.text
        return actual_text
        
    #7.COnfirm product is available
    def confirm_if_product_is_Available():
        message_locator = Text("Checkout")
        wait_until(message_locator.exists, timeout_secs= 10)
        actual_text = message_locator.web_element.text
        return actual_text
    
    #8.Click Proced to checkout
    
    def checkout():
        click("Checkout")
    #9.Check Checkou page is visible.
    
    def Check_if_checkout_if_available():
        message_locator = Text("Pay Now")
        wait_until(message_locator.exists, timeout_secs= 10)
        actual_text = message_locator.web_element.text
        return actual_text
        
    #10.
 