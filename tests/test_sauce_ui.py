from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.finish_page import FinishPage

def test_full_checkout_flow(browser, config):
    browser.get(config["base_url"])

    login = LoginPage(browser)
    inventory = InventoryPage(browser)
    cart = CartPage(browser)
    checkout = CheckoutPage(browser)
    finish = FinishPage(browser)

    login.login(config["username"], config["password"])
    inventory.add_product("Sauce Labs Backpack")
    inventory.add_product("Sauce Labs Bike Light")
    inventory.go_to_cart()
    cart.checkout()
    checkout.fill_info("John", "Doe", "12345")
    finish.finish()
    assert finish.get_success_message() == "Thank you for your order!"
