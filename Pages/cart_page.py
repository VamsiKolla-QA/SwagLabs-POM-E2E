import time

from selenium.webdriver.common.by import By

from Pages.base_page import BasePage
from Utility.utility import Utility


class CartPage(BasePage):
    # -------------------------------
    # Locators for cart elements
    # -------------------------------
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        super().__init__(driver)

    def is_cart_page_loaded(self):
        """
        Verify if the cart page is loaded successfully.
        """
        try:
            # First check if title is visible and has correct text
            title_element = Utility.wait_for_element_visible(self.driver, self.CART_TITLE)
            if not (title_element.is_displayed() and title_element.text == "Your Cart"):
                return False

            # Then check if checkout button is visible
            checkout_button = Utility.wait_for_element_visible(self.driver, self.CHECKOUT_BUTTON)
            return checkout_button.is_displayed()
        except Exception:
            return False

    def click_checkout(self):
        """
        Click the checkout button using JavaScript.
        """
        try:
            # Locate the checkout button by its ID
            checkout_button = self.driver.find_element(*self.CHECKOUT_BUTTON)
            # Use JavaScript to click the checkout button
            self.driver.execute_script("arguments[0].click();", checkout_button)
            # Briefly pause to allow any subsequent page transition to occur
            time.sleep(1)
            print("Clicked the checkout button using JavaScript.")
            return True
        except Exception as e:
            print(f"Error clicking the checkout button: {str(e)}")
            return False
