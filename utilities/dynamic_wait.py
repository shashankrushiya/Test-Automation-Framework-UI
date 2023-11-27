from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_helper(func):
    def wrapper(*args, **kwargs):      # args --> (self: instance_address, locator:tuple). kwargs --> value
        instance, locator = args
        wait_object = WebDriverWait(instance.driver, timeout=10)
        wait_object.until(EC.visibility_of_element_located(locator))
        return func(*args, **kwargs)        # enter_text
    return wrapper

