from POM.HomePage import *
from POM.LoginPage import *
from POM.SauceLabsBackpack import *
from POM.CartPage import *
from POM.CheckoutPage import *

def test_case2(setup):
    driver=setup
    l=LoginPage(driver)
    l.username("standard_user")
    l.password("secret_sauce")
    l.login_button()
    h = HomePage(driver)
    h.sauce_lab_backpack()
    slb=SauceLabsBackpack(driver)
    slb.add_to_cart()
    slb.cart_icon()
    crt=CartPage(driver)
    crt.checkout()
    cout=Checkoutpage(driver)
    cout.first_name("eisa")
    cout.last_name("abdullah")
    cout.postal_code("629002")
    cout.continue_button()
    cout.finish_button()
