from selenium.webdriver.support.select import Select
from selenium.webdriver import Chrome
driver=Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys("standard_user")
driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("secret_sauce")
driver.find_element_by_xpath("//input[@type='submit']").click()

dd = driver.find_element_by_xpath("//select[@class='product_sort_container']")
s = Select(dd)
s.select_by_visible_text("Price (low to high)")
prices =driver.find_elements_by_xpath("//div[@class='inventory_item_price']")
n=[]
for price in prices:
    s=price.text
    m=s.strip("$")
    n.append(float(m))
print(n)
assert n[0]<n[1] , "Items not sorted"
driver.quit()