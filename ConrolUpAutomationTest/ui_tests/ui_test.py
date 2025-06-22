from selenium.webdriver.common.by import By
from ui_tests.ui_test_components import UITestComponents

class TestsUI:

    USER_NAME = 'standard_user'
    PASSWORD = 'secret_sauce'
    test_components = UITestComponents()

    def test_login_and_verify_inventory(self):
        """
        Navigate to https://www.saucedemo.com and log in
        Verify that the inventory page displays exactly 6 items
        """
        self.test_components.setup()
        self.test_components.login(self.USER_NAME, self.PASSWORD)
        self.test_components.wait_for_new_page("inventory_container")
        assert self.test_components.get_elements_by_class("inventory_item").__len__() == 6
        self.test_components.quit_driver()

    def test_add_first_item_to_cart(self):
        """
        Log in as described in Scenario 1.
        Add the first inventory item to the shopping cart.
        Verify that the cart badge correctly displays the number 1.
        """
        self.test_components.setup()
        self.test_components.login(self.USER_NAME, self.PASSWORD)

        self.test_components.wait_for_new_page("inventory_container")
        inventory_container = self.test_components.get_elements_by_class("inventory_item")
        inventory_item_description = inventory_container[0].find_element(By.CLASS_NAME, "inventory_item_description")
        price_bar = inventory_item_description.find_element(By.CLASS_NAME, "pricebar")
        add_to_cart_btn = price_bar.find_element(By.CLASS_NAME, "btn_inventory")
        add_to_cart_btn.click()

        shopping_cart_span = self.test_components.get_element_by_class("shopping_cart_badge")
        assert shopping_cart_span.text == "1"
        self.test_components.quit_driver()
