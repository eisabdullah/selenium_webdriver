class LoginPage:
    def __init__(self,driver):
        self.driver=driver
    def username(self,un):
        self.driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(un)
    def password(self,pwd):
        self.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(pwd)
    def login_button(self):
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
