from datetime import datetime
from config.config import Config
from pages.ebay_homepage import HomePage


def test_access_product_via_search(driver_):
    try:
        hopmepage = HomePage(driver_)

        # ----------------Searching Product------------
        hopmepage.click_search_bar()
        hopmepage.search_product("MacBook")
        hopmepage.click_search_btn()

        # -----------------Navigating to Computers/Tablets & Networking -----------
        hopmepage.click_computer_category()

        # -----------------Verify page loads completely-------------------
        hopmepage.verify_page_load()

        # -----------------Validating First Product----------------
        hopmepage.verify_search_string_first_result()

    except Exception as exception_message:
        today = datetime.now()

        # ---------------Save screenshot in case of any Error ----------------
        driver_.save_screenshot(Config.screenshot_path + f"screenshot1-{today.day}-{today.second}.png")

        raise exception_message
