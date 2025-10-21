from utils.locator_loader import locator_loader
from playwright.sync_api import expect
class LoginPage:
    locators=locator_loader("config/locators.csv")
    def __init__(self,page):
        self.page=page
      
        self.username_input=page.locator(self.locators["username_input"]["selector_value"])
        self.password_input=page.locator(self.locators["password_input"]["selector_value"])
        self.login_button=page.locator(self.locators["login_btn"]["selector_value"])
        self.logo=page.locator(self.locators["logo"]["selector_value"])
        
    def navigate(self):
        try:
         self.page.goto("https://www.saucedemo.com")
        except:
            print("Error on navigation.")
        
    def login(self,username,password):
        try:
         self.username_input.fill(username)
         self.password_input.fill(password)
         self.page.screenshot(path="photos/login.png",full_page=True)
         self.login_button.click()
         self.page.wait_for_selector(self.locators["inventory_list"]["selector_value"])
         expect(self.logo).to_have_text("Swag Labs")

        except:
            print("Error in login.")
        