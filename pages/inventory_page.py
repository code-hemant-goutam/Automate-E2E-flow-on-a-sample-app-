class Inventory_page:
    def __init__(self,page):
        self.page=page
        self.cart_icon = page.locator("#shopping_cart_container a")
        
    def add_item_to_cart(self,item_name):
        item=self.page.get_by_text(item_name)
        item.scroll_into_view_if_needed()
        self.page.locator("button[id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
        
    def go_to_cart(self):
        self.cart_icon.click()
        
