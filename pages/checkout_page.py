class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_btn = page.locator("#continue")
        self.finish_btn = page.locator("#finish")
        self.success_header = page.locator(".complete-header")

    def fill_details_and_finish(self, first, last, postal):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)
        self.continue_btn.click()
        self.finish_btn.click()

    def verify_order_success(self):
        text = self.success_header.inner_text().strip()
        assert "Thank you for your order!" in text
