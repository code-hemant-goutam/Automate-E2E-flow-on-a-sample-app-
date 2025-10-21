import json
import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import Inventory_page
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

with open("config/credentials.json") as f:
    creds = json.load(f)

test_data = [
    (creds["username"], creds["password"], True),          
    ("invalid_user", creds["password"], False),           
    ]                   


@pytest.mark.parametrize("username,password,is_valid", test_data)
def test_purchase_flow(page, username, password, is_valid):
    login_page = LoginPage(page)
    inventory_page = Inventory_page(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.navigate()

    if is_valid:
        login_page.login(username, password)
        inventory_page.add_item_to_cart("Test.allTheThings() T-Shirt (Red)")
        inventory_page.go_to_cart()
        cart_page.proceed_to_checkout()
        checkout_page.fill_details_and_finish("Hemant", "Goutam", "202101")
        checkout_page.verify_order_success()
    else:
        try:
            login_page.login(username, password)
            error_locator = page.locator('[data-test="error"]')
            expect(error_locator).to_be_visible()
            print(f"Login failed as expected for user: {username}")
        except Exception as e:
            print(f"Expected login failure for user {username}: {e}")
