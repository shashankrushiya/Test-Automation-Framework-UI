from config.config import Config as c
from utilities.generic import SeleniumWrapper


class HomePage(SeleniumWrapper):
    def click_shop_by_category(self):
        self.click_on_element(c.shop_by_category)

    def click_cell_phone_accessories(self):
        self.click_on_element(c.cell_phone_accessories)

    def asserting_filters(self):
        self.verify_condition_applied(c.condition_check)
        self.verify_price_applied(c.price_check)
        self.verify_location_applied(c.item_location_check)

    def click_search_bar(self):
        self.click_on_element(c.search_bar)

    def search_product(self, product):
        self.enter_text(c.search_bar, value=product)

    def click_search_btn(self):
        self.click_on_element(c.search_button)

    def click_computer_category(self):
        self.click_on_element(c.category)

    def verify_search_string_first_result(self):
        self.verify_product(c.first_product)





