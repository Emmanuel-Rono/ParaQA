
import os
from helium import go_to, start_chrome, write, click, Text, S, find_all, wait_until, kill_browser,text
from faker import Faker


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
    #Check that product details are displayed
    #3.Add to cart
    #5.Check if cart appears as slideing window
    #6.View Cart
    #7.COnfirm product is available
    #8.Click Proced to checkout
    #9.Check Checkou page is visible.
    #10.
        
    
    