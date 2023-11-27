from config.config import Config as c
from utilities.generic import SeleniumWrapper


class FilterBox(SeleniumWrapper):
    def select_filter(self, apply_filter):
        self.move_to_element(c.all_filters, value=apply_filter)

    def select_openbox_checkbox(self):
        self.click_on_element(c.openbox_checkbox)

    def enter_min_price(self, price):
        self.enter_text(c.min_price, value=price)

    def enter_max_price(self, price):
        self.enter_text(c.max_price, value=price)

    def select_worldwide_location(self):
        self.click_on_element(c.worldwide)

    def click_apply(self):
        self.click_on_element(c.apply_btn)

