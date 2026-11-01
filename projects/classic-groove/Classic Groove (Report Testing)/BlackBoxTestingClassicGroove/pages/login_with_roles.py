import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.base_driver import chrome_driver


def wait_for_clickable_element(chrome_driver, locator, timeout=10):
    """Wait for an element to be clickable and return it."""
    wait = WebDriverWait(chrome_driver, timeout)
    return wait.until(EC.element_to_be_clickable(locator))

# Helper function for clicking an element
def click_element(chrome_driver, element):
    """Click an element safely."""
    chrome_driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

def loginRoleInAdmin(chrome_driver, username, role):
    # Navigate to the website
    chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div').click()
    time.sleep(2)

    login = wait_for_clickable_element(chrome_driver, (By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input'))
    click_element(chrome_driver, login)
    time.sleep(2)

    chrome_driver.find_element(By.XPATH, '//*[@id="username-field"]').send_keys("lahieuphong_superAdmin")
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field"]').send_keys("Tatooboys123@")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[1]/form/div[3]/input').click()
    time.sleep(2)

    # Navigate to account section
    chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[4]').click()
    time.sleep(3)
    # Find all account items
    accounts = chrome_driver.find_elements(By.CLASS_NAME, 'item')

    account_found = False

    for i in range(0, len(accounts), 7):  # Assuming each account takes 7 'item' divs
        account_username = accounts[i + 1].text.strip()  # Extract username
        account_role = accounts[i + 4].text.strip()  # Extract role

        # Check if the current account matches the input parameters
        if account_username == username and account_role == role:
            account_found = True
            break

    # Assert the account is found
    assert account_found, f"Account with username '{username}' and role '{role}' not found in the list."