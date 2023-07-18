from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self,driver):
        self.driver=driver
    def twitter(self):
        self.driver.implicitly_wait(5)
        tweet=self.driver.find_element_by_xpath("//img[@alt='Twitter']")
        loc=tweet.location
        self.driver.execute_script(f"window.scrollBy({loc['x']},{loc['y']})")
        self.driver.find_element_by_xpath("//button[.='OK']").click()
        tweet.click()

    def solutions(self):
        a=ActionChains(self.driver)
        solution=self.driver.find_element_by_xpath("//span[.='Solutions']")
        a.move_to_element(solution).perform()
    def automation_tools(self):
        self.driver.find_element_by_xpath("//span[.='Automation tools']").click()
        tabs=self.driver.window_handles
        for tab in tabs:
            self.driver.switch_to.window(tab)
