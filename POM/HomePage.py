from selenium.webdriver.support.select import Select
class HomePage:
    def __init__(self,driver):
        self.driver=driver
    def hamburger(self):
        self.driver.find_element_by_xpath("//button[.='Open Menu']").click()
    def logout_button(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//a[.='Logout']").click()
    def sauce_lab_backpack(self):
        self.driver.find_element_by_xpath("//div[.='Sauce Labs Backpack']").click()

    def sort_dd(self):
        dd=self.driver.find_element_by_xpath("//select[@class='product_sort_container']")
        s=Select(dd)
        s.select_by_visible_text("Price (low to high)")
        prices = self.driver.find_elements_by_xpath("//div[@class='inventory_item_price']")
        n = []
        for price in prices:
            s = price.text
            m = s.strip("$")
            n.append(float(m))
        print(n)
        assert n[0] < n[1], "Items not sorted"

    def about(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//a[.='About']").click()