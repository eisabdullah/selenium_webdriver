from POM.LoginPage import *
from POM.HomePage import *
from time import sleep

def test_case1(setup):
    driver=setup
    l=LoginPage(driver)
    l.username("standard_user")
    l.password("secret_sauce")
    l.login_button()
    h=HomePage(driver)
    h.hamburger()
    h.logout_button()