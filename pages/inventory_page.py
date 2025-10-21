from utils.locator_loader import locator_loader
from playwright.sync_api import expect
class Inventory_page:
    locators=locator_loader("config/locators.csv")

    def __init__(self,page):
        self.page=page
        try:
         self.cart_icon = page.locator(self.locators["cart_icon"]["selector_value"])
         self.cart_badge=page.locator(self.locators["cart_badge"]["selector_value"])
        except:
            print("Not able to find locator for cart icon.")
            
    def add_item_to_cart(self,item_name):
        try:            
         item1=self.page.get_by_text(item_name)
         item1.scroll_into_view_if_needed()
         self.page.locator(self.locators["red_tshirt"]["selector_value"]).click()
         self.page.screenshot(path="photos/add_to_cart.png",full_page=True)

         self.page.get_by_text(self.locators["add_to_cart_text"]["selector_value"]).first.click()
         expect(self.cart_badge).to_have_text("2")

        except:
            print("Failed to add item to cart.")
        
    def go_to_cart(self):
        try:
         self.cart_icon.click()
         self.page.screenshot(path="photos/cart_page.png",full_page=True)

        except:
            print("Failed on navigation to cart.")
