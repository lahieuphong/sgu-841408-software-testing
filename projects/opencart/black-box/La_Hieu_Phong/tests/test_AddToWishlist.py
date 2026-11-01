from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    """Fixture to initialize the WebDriver."""
    driver = webdriver.Chrome()  # Initialize the Chrome WebDriver
    yield driver  # Yield the driver to the test
    driver.quit()  # Quit the WebDriver after the test


def wait_for_element(driver, by, value, timeout=5):
    """Wait for an element to be clickable and return it."""
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.element_to_be_clickable((by, value)))


def wait_for_visibility(driver, by, value, timeout=5):
    """Wait for an element to be visible and return it."""
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.visibility_of_element_located((by, value)))


def login(driver):
    """Log in to OpenCart."""
    driver.get("http://localhost/demo/index.php?route=account/login&language=en-gb")
    time.sleep(1)  # Allow page to load

    email_field = wait_for_visibility(driver, By.ID, "input-email")
    email_field.send_keys("hieuphong144@gmail.com")

    password_field = wait_for_visibility(driver, By.ID, "input-password")
    password_field.send_keys("21112003")

    login_button = wait_for_element(driver, By.CSS_SELECTOR, "button.btn.btn-primary")
    login_button.click()

    # Wait for the page title to contain "My Account" to confirm successful login
    WebDriverWait(driver, 5).until(EC.title_contains("My Account"))


def add_to_wishlist_without_login(driver):
    """Add a product to the wishlist without logging in."""
    driver.get("http://localhost/demo/index.php?route=product/product&language=en-gb&product_id=40&search=iphone")
    time.sleep(2)  # Allow page to load

    wishlist_button = wait_for_element(driver, By.CSS_SELECTOR, "button.btn.btn-light[data-bs-toggle='tooltip']")
    wishlist_button.click()
    time.sleep(2)

    alert_message = wait_for_visibility(driver, By.CSS_SELECTOR, "div.alert-success")
    assert "You must login" in alert_message.text, "Expected login message not found."


def add_to_wishlist_with_login(driver):
    """Add a product to the wishlist after logging in."""
    driver.get("http://localhost/demo/index.php?route=product/product&language=en-gb&product_id=40&search=iphone")
    time.sleep(2)

    # Get product details from the product page
    product_name_element = wait_for_visibility(driver, By.XPATH, '//*[@id="content"]/div[1]/div[2]/h1')
    product_name = product_name_element.text

    product_price_element = wait_for_visibility(driver, By.XPATH, '//*[@id="content"]/div[1]/div[2]/ul[2]/li[1]/h2/span')
    product_price = product_price_element.text

    # Add product to the wishlist
    wishlist_button = wait_for_element(driver, By.CSS_SELECTOR, "button.btn.btn-light[data-bs-toggle='tooltip']")
    wishlist_button.click()
    time.sleep(8)

    # Navigate to the wishlist page
    wishlist_button_header = wait_for_element(driver, By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[3]')
    wishlist_button_header.click()

    # Verify product details in the wishlist
    wishlist_name_element = wait_for_visibility(driver, By.XPATH, '//*[@id="wishlist"]/div/table/tbody/tr/td[2]/a')
    wishlist_name = wishlist_name_element.text

    wishlist_price_element = wait_for_visibility(driver, By.XPATH, '//*[@id="wishlist"]/div/table/tbody/tr/td[5]/div')
    wishlist_price = wishlist_price_element.text

    assert product_name == wishlist_name, f"Product name mismatch: {product_name} != {wishlist_name}"
    assert product_price == wishlist_price, f"Product price mismatch: {product_price} != {wishlist_price}"


def test_add_to_wishlist_without_login(driver):
    """Test adding a product to the wishlist without being logged in."""
    add_to_wishlist_without_login(driver)


def test_add_to_wishlist_with_login(driver):
    """Test adding a product to the wishlist after logging in."""
    login(driver)
    time.sleep(3)
    add_to_wishlist_with_login(driver)