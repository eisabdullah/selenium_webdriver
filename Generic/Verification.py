from Generic.Screenshot import take_screenshot
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def verify_text(loc,etext,driver):
    wait=WebDriverWait(driver,10)
    try:
        wait.until(EC.text_to_be_present_in_element(loc,etext))
    except:
        take_screenshot(driver)
        raise Exception("text not found")

def verify_title(title,driver):
    wait=WebDriverWait(driver,10)
    try:
        wait.until(EC.title_is(title))
    except:
        take_screenshot(driver)
        raise Exception("Page error ")



