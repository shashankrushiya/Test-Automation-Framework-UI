from datetime import datetime

import pytest

from config.config import Config
from pages.ebay_homepage import HomePage
from pages.ebay_cell_phone_accessories import CellPhoneAccessories
from pages.ebay_filter_box import FilterBox


@pytest.mark.xfail
def test_access_via_category(driver_):
    try:
        homepage = HomePage(driver_)
        cell_phone_accessories_page = CellPhoneAccessories(driver_)
        filterbox = FilterBox(driver_)

        # --------------------Selecting Category--------------------
        homepage.click_shop_by_category()
        homepage.click_cell_phone_accessories()

        # --------------------Clicking All filters--------------------------
        cell_phone_accessories_page.click_cell_phone_smartphones()
        cell_phone_accessories_page.scroll_to_all_filters()
        cell_phone_accessories_page.click_all_filters()

        # --------------------Applying filters--------------------------
        filterbox.select_filter("Condition")
        filterbox.select_openbox_checkbox()
        filterbox.select_filter("Price")
        filterbox.enter_min_price("100")
        filterbox.enter_max_price("500")
        filterbox.select_filter("Item Location")
        filterbox.select_worldwide_location()
        filterbox.click_apply()

        # ----------------------Verifying filters applied--------------
        homepage.asserting_filters()

    except Exception as exception_message:
        today = datetime.now()
        # ---------------Save screenshot in case of any Error ----------------
        driver_.save_screenshot(Config.screenshot_path + f"screenshot1-{today.day}-{today.second}.png")

        raise exception_message
