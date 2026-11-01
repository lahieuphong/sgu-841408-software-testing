from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
import time
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Initialize the Chrome WebDriver
    yield driver  # Yield the driver for use in tests
    driver.quit()  # Close the driver after the test


# Test case for writing a review
def test_WriteReview(driver):
    driver.get("http://localhost/demo/index.php?route=account/login&language=en-gb")  # Open the login page of OpenCart

    wait = WebDriverWait(driver, 2)  # Set up a WebDriverWait for 2 seconds

    # Wait for the email field to be visible and enter email
    emailField = wait.until(EC.visibility_of_element_located((By.ID, "input-email")))
    emailField.send_keys("hieuphong144@gmail.com")

    # Wait for the password field to be visible and enter the password
    passwordField = wait.until(EC.visibility_of_element_located((By.ID, "input-password")))
    passwordField.send_keys("21112003")
    time.sleep(2)  # Pause for 2 seconds

    # Wait for the login button to be clickable and click it
    loginButton = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    loginButton.click()

    # Wait until the page title contains "My Account"
    wait.until(EC.title_contains("My Account"))
    time.sleep(2)  # Pause for 2 seconds

    # Navigate to the homepage and then to the product page
    driver.get("http://localhost/demo/index.php?route=common/home&language=en-gb")
    time.sleep(2)

    driver.get("http://localhost/demo/index.php?route=product/product&language=en-gb&product_id=40&search=iphone")
    time.sleep(2)

    # Wait for the "Write a review" link to be clickable and click it
    writeReviewLink = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Write a review"))
    )
    driver.execute_script("arguments[0].click();", writeReviewLink)
    time.sleep(2)

    # Wait for the review text area to be visible and enter review text
    reviewTextArea = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-text"))
    )
    reviewTextArea.send_keys("This is my review text.")
    time.sleep(2)

    # Scroll down to ensure the rating options are visible
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")

    time.sleep(1)  # Wait for the scroll to take effect

    # Select a rating (e.g., 5 stars)
    ratingRadioButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='rating'][value='5']"))
    )
    ratingRadioButton.click()
    time.sleep(1)

    # Wait for the "Continue" button to be clickable and click it
    submitButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "button-review"))
    )
    submitButton.click()
    time.sleep(2)  # Pause to allow the action to be completed

    print("Still not redirecting the page")