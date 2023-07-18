from Generic.Verification import *
class Checkoutpage:
    def __init__(self,driver):
        self.driver=driver
    def first_name(self,fn):
        self.driver.find_element_by_xpath("//input[@id='first-name']").send_keys(fn)
    def last_name(self,ln):
        self.driver.find_element_by_xpath("//input[@id='last-name']").send_keys(ln)
    def postal_code(self,pc):
        self.driver.find_element_by_xpath("//input[@id='postal-code']").send_keys(pc)
    def continue_button(self):
        self.driver.find_element_by_xpath("//input[@id='continue']").click()
    def finish_button(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//button[@id='finish']").click()
        loc=("xpath","//h2")
        verify_text(loc,"Thank you for your order!",self.driver)


