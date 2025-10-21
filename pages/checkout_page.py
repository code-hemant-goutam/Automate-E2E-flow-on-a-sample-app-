from utils.locator_loader import locator_loader
class CheckoutPage:
    locators=locator_loader("config/locators.csv")
    def __init__(self, page):
        try:
         self.page = page
         self.first_name = page.locator(self.locators["first_name"]["selector_value"])
         self.last_name = page.locator(self.locators["last_name"]["selector_value"])
         self.postal_code = page.locator(self.locators["postal_code"]["selector_value"])
         self.continue_btn = page.locator(self.locators["continue_btn"]["selector_value"])
         self.finish_btn = page.locator(self.locators["finish_btn"]["selector_value"])
         self.success_header = page.locator(self.locators["success_header"]["selector_value"])
        except:
            print("Failed on finding locators.")
            
    def fill_details_and_finish(self, first, last, postal):
        try:
         self.first_name.fill(first)
         self.last_name.fill(last)
         self.postal_code.fill(postal)
         self.continue_btn.click()
         self.page.screenshot(path="photos/make_order.png",full_page=True)

         self.finish_btn.click()
        except:
            print("Error on finish step.")

    def verify_order_success(self):
        try:            
         text = self.success_header.inner_text().strip()
         self.page.screenshot(path="photos/order_placed.png",full_page=True)

         assert self.locators["thank_you_text"]["selector_value"] in text
        except:
            print("Failed to verify order success.")