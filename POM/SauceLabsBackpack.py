class SauceLabsBackpack:
    def __init__(self,driver):
        self.driver=driver
    def add_to_cart(self):
        self.driver.find_element_by_xpath("//button[.='Add to cart']").click()
    def cart_icon(self):
        self.driver.find_element_by_xpath("//a[@class='shopping_cart_link']").click()