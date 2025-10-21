from utils.locator_loader import locator_loader
class CartPage:
    locators=locator_loader("config/locators.csv")    
    def __init__(self, page):
        self.page = page
        try:
         self.checkout_button = page.locator(self.locators["checkout_btn"]["selector_value"])
        except:
            print("Failed to find locator for checkout button.")
            
    def proceed_to_checkout(self):
        try:
         self.checkout_button.click()
        except:
            print("Error on checkout.")