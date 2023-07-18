class CartPage:
    def __init__(self,driver):
        self.driver=driver
    def checkout(self):
        self.driver.find_element_by_xpath("//button[.='Checkout']").click()
        