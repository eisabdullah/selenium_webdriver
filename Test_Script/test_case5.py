from POM.LoginPage import *
from POM.HomePage import *
from POM.BasePage import *
from Generic.Verification import verify_title

def test_case4(setup):
    driver=setup
    l=LoginPage(driver)
    l.username("standard_user")
    l.password("secret_sauce")
    l.login_button()
    h=HomePage(driver)
    h.hamburger()
    h.about()
    b=BasePage(driver)
    b.solutions()
    b.automation_tools()
    verify_title("Getting Started with Sauce Labs Integrations | Sauce Labs Documentation",driver)