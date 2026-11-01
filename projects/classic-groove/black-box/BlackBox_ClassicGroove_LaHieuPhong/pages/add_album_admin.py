from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.base_driver import chrome_driver


# Helper function for waiting for clickable elements
def wait_for_clickable_element(chrome_driver, locator, timeout=10):
    wait = WebDriverWait(chrome_driver, timeout)
    return wait.until(EC.element_to_be_clickable(locator))


# Helper function for clicking an element
def click_element(chrome_driver, element):
    chrome_driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()