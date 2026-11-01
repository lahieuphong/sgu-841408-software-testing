import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.base_driver import chrome_driver
from pages.navigate import navigate_to_index_page
from pages.register import get_notice_text, generate_random_username


def test_registerValid(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)

    # Wait for and click the signup button
    WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[2]/input'))).click()
    time.sleep(2)

    # Perform login (registration)
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/input[1]').send_keys("Thảo Nguyên")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/input[2]').send_keys("0332569916")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/input[3]').send_keys("Thảo Nguyênn")
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field2"]').send_keys("123Nguyen!")
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field3"]').send_keys("123Nguyen!")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/div[3]/input').click()
    time.sleep(2)  # Wait for the registration to process

    notice_text = get_notice_text(chrome_driver)

    # Assert if account is successfully created or username already exists
    if "Accout successfully created!" in notice_text:  # Note the typo in the message
        print("Account created successfully!")
        assert "Accout successfully created!" in notice_text, "Account creation failed"
    elif "Username already exists!" in notice_text:
        print("Username already exists!")
        assert "Username already exists!" in notice_text, "Account creation failed"
    else:
        print("Unexpected notice message:", notice_text)
        assert False, "Unexpected message received during registration process"


def test_registerEmptyUsername(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)

    # Wait for and click the signup button
    WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[2]/input'))).click()
    time.sleep(2)

    # Perform login
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/input[1]').send_keys("Thảo Nguyên")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/input[2]').send_keys("0332569916")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/input[3]').send_keys("")
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field2"]').send_keys("123Nguyen!")
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field3"]').send_keys("123Nguyen!")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/div[3]/input').click()
    time.sleep(2)

    notice_text = get_notice_text(chrome_driver)

    # Assert that the notice message is correct (username not entered)
    assert "Please, enter username!" in notice_text, f"Expected message 'Please, enter username!', but got: {notice_text}"


def test_registerPasswordNoSpecialCharacters(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)

    # Wait for and click the login button
    WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[2]/input'))).click()
    time.sleep(2)

    # Perform login
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/input[1]').send_keys("Thảo Nguyên")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/input[2]').send_keys("0332569916")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/input[3]').send_keys("Thảo Nguyên1")
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field2"]').send_keys("123Nguyen")
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field3"]').send_keys("123Nguyen")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/div[3]/input').click()
    time.sleep(2)

    notice_text = get_notice_text(chrome_driver)

    # Assert that the notice message is correct (username not entered)
    assert "Password that contain at least eight characters, including at least one number and includes both lowercase and uppercase letters and special characters, for example #, ?, !." in notice_text, f"Expected message 'Password that contain at least eight characters, including at least one number and includes both lowercase and uppercase letters and special characters, for example #, ?, !.', but got: {notice_text}"


def test_registerUsernameNoSpecialCharacters(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)

    # Wait for and click the signup button
    WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[2]/input'))).click()
    time.sleep(2)

    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/input[1]').send_keys("Thảo Nguyên")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/input[2]').send_keys("0332569916")
    random_username = generate_random_username(12)  # Tạo tên người dùng ngẫu nhiên dài 12 ký tự
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/input[3]').send_keys(random_username)
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field2"]').send_keys("123Nguyen!")
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field3"]').send_keys("123Nguyen!")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/div[3]/input').click()
    time.sleep(2)

    notice_text = get_notice_text(chrome_driver)

    # Assert that the notice message is correct (username not entered or username has invalid characters)
    assert "Username does not have characters" in notice_text, \
        f"Expected message 'Username does not have characters', but got: {notice_text}"


def test_registerUsernameIsTooLong(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)

    # Wait for and click the login button
    WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[2]/input'))).click()
    time.sleep(2)

    # Perform login
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/input[1]').send_keys("Thảo Nguyên")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/input[2]').send_keys("0332569916")
    random_username = generate_random_username(100)  # Tạo tên người dùng ngẫu nhiên dài 100 ký tự
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/input[3]').send_keys(random_username)
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field2"]').send_keys("123Nguyen!")
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field3"]').send_keys("123Nguyen!")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/div[3]/input').click()
    time.sleep(2)

    notice_text = get_notice_text(chrome_driver)

    # Assert that the notice message is correct (username not entered)
    assert "username is too long" in notice_text, f"username is too long', but got: {notice_text}"


def test_registerSQL(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)

    # Wait for and click the login button
    WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[2]/input'))).click()
    time.sleep(2)

    # Perform login
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/input[1]').send_keys("Thảo Nguyên")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/input[2]').send_keys("0332569916")

    # Try SQL Injection by sending a payload
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/input[3]').send_keys("' OR 1=1 --")
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field2"]').send_keys("123Nguyen!")
    chrome_driver.find_element(By.XPATH, '//*[@id="password-field3"]').send_keys("123Nguyen!")
    chrome_driver.find_element(By.XPATH, '//*[@id="login"]/div/div[2]/form/div[3]/input').click()
    time.sleep(2)

    notice_text = get_notice_text(chrome_driver)

    # Assert that the notice message is correct
    assert "You cannot use special characters" in notice_text, f"Expected 'You cannot use special characters', but got: {notice_text}"