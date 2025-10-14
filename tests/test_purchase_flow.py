from pages.login_page import LoginPage
from pages.inventory_page import Inventory_page
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_purchase_flow(page):
    login_page=LoginPage(page)
    inventory_page=Inventory_page(page)
    cart_page=CartPage(page)
    checkout_page=CheckoutPage(page)
    
    login_page.navigate()
    
    login_page.login("standard_user","secret_sauce")
    inventory_page.add_item_to_cart("Test.allTheThings() T-Shirt (Red)")
    inventory_page.go_to_cart()
    cart_page.proceed_to_checkout()
    checkout_page.fill_details_and_finish("Hemant","Goutam","202101")
    checkout_page.verify_order_success()