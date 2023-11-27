import time

from utilities.dynamic_wait import wait_helper


class SeleniumWrapper:

    def __init__(self, driver):
        self.driver = driver

    @wait_helper
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @wait_helper
    def enter_text(self, locator, *, value):
        self.driver.find_element(*locator).send_keys(value)

    @wait_helper
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)

        try:
            self.driver.execute_script("arguments[0].scrollIntoView()", element)

        except:
            print("Unable to scroll")

    @wait_helper
    def move_to_element(self, locator, value):
        filters = self.driver.find_elements(*locator)
        for filter_ in filters:
            if filter_.text == value:
                filter_.click()

    @wait_helper
    def verify_condition_applied(self, locator):
        condition = self.driver.find_element(*locator)
        assert "Open box" in condition.text, "Condition filter not applied"
        print("Condition filter applied")

    @wait_helper
    def verify_price_applied(self, locator):
        price = self.driver.find_element(*locator)
        assert "$100.00 to $500.00" in price.text, "Price filter not applied"
        print("Price filter applied")

    @wait_helper
    def verify_location_applied(self, locator):
        location = self.driver.find_element(*locator)
        assert "Worldwide" in location.text, "Item Location filter not applied"
        print("Location filter applied")

    def verify_page_load(self):
        time.sleep(2)
        ready_state = self.driver.execute_script("return document.readyState")
        if ready_state == "complete":
            print("The page has loaded completely.")
        else:
            print("The page is still loading.")

    def verify_product(self, locator):
        first_item = self.driver.find_element(*locator)
        assert "MacBook" in first_item.text, "Search string mismatched"
        print("Search String is Verified")
