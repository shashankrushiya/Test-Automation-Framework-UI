class Config:
    # -------URL-----------------------------------------------------
    url = "https://www.ebay.com/"

    # -------PATH----------------------------------------------------
    screenshot_path = r"C:\Users\User\PycharmProjects\AutomateToElevate\screenshots\\"

    # -------LOCATORS FOR EASY ACCESS--------------------------------
    shop_by_category = ("id", "gh-shop-a")
    all_filters = ('xpath', '//div[@role="tab"]//span[@class="x-overlay-aspect__label"]')
    all_filters_btn = ("xpath", '//button[text()="All Filters"]')
    applied_filter = ("xpath", '//button[@type="button"]//span[text()="3 filters applied"]')
    apply_btn = ("xpath", '//button[text()="Apply"]')
    category = ("link text", "Computers/Tablets & Networking")
    cell_phone_accessories = ("link text", "Cell phones & accessories")
    cell_phone_smartphone = ("link text", "Cell Phones & Smartphones")
    condition_check = ("xpath", '//ul[@class="brm__aspect-list"]//span[text()="Condition: Open box"]')
    first_product = ("xpath", '(//span[contains(text(), "MacBook")])[2]')
    item_location_check = ("xpath", '//ul[@class="brm__aspect-list"]//span[text()="Item Location: '
                                    'Worldwide"]')
    max_price = ("xpath", '//div[@id="c3-subPanel-_x-price-textrange"]//input['
                          '@class="x-textrange__input x-textrange__input--to"]')
    min_price = ("xpath", '//div[@id="c3-subPanel-_x-price-textrange"]//input['
                          '@class="x-textrange__input x-textrange__input--from"]')
    openbox_checkbox = ("xpath", "//span[@class='cbx x-refine__multi-select-cbx'][normalize-space("
                                 ")='Open box']")
    price_check = ("xpath", '//ul[@class="brm__aspect-list"]//span[text()="Price: $100.00 to $500.00"]')
    search_bar = ('id', 'gh-ac')
    search_button = ("id", "gh-btn")
    worldwide = ("xpath", "//input[@value='Worldwide']")
