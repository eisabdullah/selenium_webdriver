from POM.LoginPage import *
from POM.HomePage import *
from time import sleep

def test_case2(setup):
    driver=setup
    l=LoginPage(driver)
    l.username("standard_user")
    l.password("secret_sauce")
    l.login_button()
    h = HomePage(driver)
    h.sort_dd()

