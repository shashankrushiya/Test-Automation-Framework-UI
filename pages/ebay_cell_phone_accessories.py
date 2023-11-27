from config.config import Config as c
from utilities.generic import SeleniumWrapper


class CellPhoneAccessories(SeleniumWrapper):
    def click_cell_phone_smartphones(self):
        self.click_on_element(c.cell_phone_smartphone)

    def scroll_to_all_filters(self):
        self.scroll_to_element(c.all_filters_btn)

    def click_all_filters(self):
        self.click_on_element(c.all_filters_btn)
