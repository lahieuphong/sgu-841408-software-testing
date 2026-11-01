import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.base_driver import chrome_driver
from pages.login import login_success_superAdmin
from pages.navigate import navigate_to_index_page


def test_edit_account_full_information(chrome_driver):
    # 1. Điều hướng tới trang chủ
    navigate_to_index_page(chrome_driver)

    # 2. Đăng nhập với tư cách SuperAdmin
    login_success_superAdmin(chrome_driver)

    # 3. Nhấn vào tab "Account"
    account_tab = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'tab-title') and contains(., 'Account')]"))
    )
    account_tab.click()

    # 4. Nhấn vào nút có biểu tượng "fa-circle-info"
    info_button = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//i[contains(@class, 'fa-regular') and contains(@class, 'fa-circle-info')]"))
    )
    info_button.click()

    # 5. Nhấn vào nút "Edit"
    edit_button = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='edit-button' and contains(@onclick, \"loadModalBoxByAjax('editAccount','lahieuphong')\")]"))
    )
    edit_button.click()

    # 6. Clear và nhập lại giá trị vào ô input
    name_input = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text' and contains(@class, 'nameAccount')]"))
    )
    name_input.clear()  # Xóa nội dung hiện tại
    name_input.send_keys("La Hiểu Phong")  # Nhập lại giá trị mới

    email_input = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text' and contains(@class, 'emailAccount')]"))
    )
    email_input.clear()
    email_input.send_keys("hieuphong144@gmail.com")

    phone_input = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text' and contains(@class, 'phoneAccount')]"))
    )
    phone_input.clear()
    phone_input.send_keys("0326526898")

    password_input = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text' and contains(@class, 'passwordAccount')]"))
    )
    password_input.clear()
    password_input.send_keys("Tatooboys123@")

    address_input = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text' and contains(@class, 'addressAccount')]"))
    )
    address_input.clear()
    address_input.send_keys("abc")

    save_button = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='info-placeholder' and text()='Save']"))
    )
    save_button.click()

    time.sleep(2)

    # Chờ cho thông báo hiển thị
    notice = WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.ID, "notice")))

    # Kiểm tra thông báo 'Update successfully!'
    expected_notice = "Update successfully!"
    assert notice.is_displayed(), f"Thông báo không hiển thị. Dự kiến: {expected_notice}"
    assert notice.text == expected_notice, f"Thông báo không khớp. Dự kiến: '{expected_notice}', nhưng thực tế: '{notice.text}'"
    print(f"Thông báo hiển thị và khớp với mong đợi: {expected_notice}")

    time.sleep(5)  # You can remove or replace this if necessary for debugging

# bug: kiểm tra khi email được để trống
def test_edit_account_email_empty(chrome_driver):
    # 1. Điều hướng tới trang chủ
    navigate_to_index_page(chrome_driver)

    # 2. Đăng nhập với tư cách SuperAdmin
    login_success_superAdmin(chrome_driver)

    # 3. Nhấn vào tab "Account"
    account_tab = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'tab-title') and contains(., 'Account')]"))
    )
    account_tab.click()

    # 4. Nhấn vào nút có biểu tượng "fa-circle-info"
    info_button = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//i[contains(@class, 'fa-regular') and contains(@class, 'fa-circle-info')]"))
    )
    info_button.click()

    # 5. Nhấn vào nút "Edit"
    edit_button = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='edit-button' and contains(@onclick, \"loadModalBoxByAjax('editAccount','lahieuphong')\")]"))
    )
    edit_button.click()

    # 6. Clear và nhập lại giá trị vào ô input
    name_input = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text' and contains(@class, 'nameAccount')]"))
    )
    name_input.clear()  # Xóa nội dung hiện tại
    name_input.send_keys("La Hiểu Phong")  # Nhập lại giá trị mới

    email_input = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text' and contains(@class, 'emailAccount')]"))
    )
    email_input.clear()
    # email_input.send_keys("hieuphong144@gmail.com")

    phone_input = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text' and contains(@class, 'phoneAccount')]"))
    )
    phone_input.clear()
    phone_input.send_keys("0326526898")

    password_input = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text' and contains(@class, 'passwordAccount')]"))
    )
    password_input.clear()
    password_input.send_keys("Tatooboys123@")

    address_input = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text' and contains(@class, 'addressAccount')]"))
    )
    address_input.clear()
    address_input.send_keys("abc")

    save_button = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='info-placeholder' and text()='Save']"))
    )
    save_button.click()

    time.sleep(2)

    # Chờ cho thông báo hiển thị
    notice = WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.ID, "notice")))

    # Kiểm tra thông báo 'Please, enter your email!'
    expected_notice = "Please, enter your email!"
    assert notice.is_displayed(), f"Thông báo không hiển thị. Dự kiến: {expected_notice}"
    assert notice.text == expected_notice, f"Thông báo không khớp. Dự kiến: '{expected_notice}', nhưng thực tế: '{notice.text}'"
    print(f"Thông báo hiển thị và khớp với mong đợi: {expected_notice}")

    time.sleep(5)  # You can remove or replace this if necessary for debugging

# bug: kiểm tra khi address được để trống
def test_edit_account_address_empty(chrome_driver):
    # 1. Điều hướng tới trang chủ
    navigate_to_index_page(chrome_driver)

    # 2. Đăng nhập với tư cách SuperAdmin
    login_success_superAdmin(chrome_driver)

    # 3. Nhấn vào tab "Account"
    account_tab = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'tab-title') and contains(., 'Account')]"))
    )
    account_tab.click()

    # 4. Nhấn vào nút có biểu tượng "fa-circle-info"
    info_button = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//i[contains(@class, 'fa-regular') and contains(@class, 'fa-circle-info')]"))
    )
    info_button.click()

    # 5. Nhấn vào nút "Edit"
    edit_button = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='edit-button' and contains(@onclick, \"loadModalBoxByAjax('editAccount','lahieuphong')\")]"))
    )
    edit_button.click()

    # 6. Clear và nhập lại giá trị vào ô input
    name_input = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text' and contains(@class, 'nameAccount')]"))
    )
    name_input.clear()  # Xóa nội dung hiện tại
    name_input.send_keys("La Hiểu Phong")  # Nhập lại giá trị mới

    email_input = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text' and contains(@class, 'emailAccount')]"))
    )
    email_input.clear()
    email_input.send_keys("hieuphong144@gmail.com")

    phone_input = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text' and contains(@class, 'phoneAccount')]"))
    )
    phone_input.clear()
    phone_input.send_keys("0326526898")

    password_input = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text' and contains(@class, 'passwordAccount')]"))
    )
    password_input.clear()
    password_input.send_keys("Tatooboys123@")

    address_input = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='text' and contains(@class, 'addressAccount')]"))
    )
    address_input.clear()
    address_input.send_keys("abc")

    save_button = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='info-placeholder' and text()='Save']"))
    )
    save_button.click()

    time.sleep(2)

    # Chờ cho thông báo hiển thị
    notice = WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.ID, "notice")))

    # Kiểm tra thông báo 'Please, enter your address!'
    expected_notice = "Please, enter your address!"
    assert notice.is_displayed(), f"Thông báo không hiển thị. Dự kiến: {expected_notice}"
    assert notice.text == expected_notice, f"Thông báo không khớp. Dự kiến: '{expected_notice}', nhưng thực tế: '{notice.text}'"
    print(f"Thông báo hiển thị và khớp với mong đợi: {expected_notice}")

    time.sleep(5)  # You can remove or replace this if necessary for debugging


def test_new_account_full_information(chrome_driver):
    # 1. Điều hướng tới trang chủ
    navigate_to_index_page(chrome_driver)

    # 2. Đăng nhập với tư cách SuperAdmin
    login_success_superAdmin(chrome_driver)

    # 3. Nhấn vào tab "Account"
    account_tab = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'tab-title') and contains(., 'Account')]"))
    )
    account_tab.click()

    # 4. Nhấn vào nút có biểu tượng "fa-circle-info"
    info_button = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//i[contains(@class, 'fa-regular') and contains(@class, 'fa-circle-info')]"))
    )
    info_button.click()

    # 5. Click the "New" button using JavaScript if standard click fails
    new_button = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'new-button') and @onclick=\"loadModalBoxByAjax('newAccount')\"]")
        )
    )
    chrome_driver.execute_script("arguments[0].click();", new_button)

    # 6. Fill out the account form
    # Fill username field
    username_field = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='username']"))
    )
    username_field.send_keys("lhp")

    # Fill name field
    name_field = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='name']"))
    )
    name_field.send_keys("LHP")

    # Fill email field
    email_field = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='email']"))
    )
    email_field.send_keys("hieuphong144@gmail.com")

    # Fill phone number field
    phone_field = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='phoneNumber']"))
    )
    phone_field.send_keys("0326526898")

    # Fill password field
    password_field = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='password']"))
    )
    password_field.send_keys("Tatooboys123@")

    # Fill address field
    address_field = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='address']"))
    )
    address_field.send_keys("abc")

    # 7. Nhấn vào nút "Add" để tạo tài khoản mới
    add_button = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'edit-button') and @onclick=\"createNewAccount()\"]")
        )
    )
    chrome_driver.execute_script("arguments[0].click();", add_button)

    time.sleep(2)

    # Chờ cho thông báo hiển thị
    notice = WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.ID, "notice")))

    # Kiểm tra thông báo 'Please, enter your address!'
    expected_notice = "Account successfully created"
    assert notice.is_displayed(), f"Thông báo không hiển thị. Dự kiến: {expected_notice}"
    assert notice.text == expected_notice, f"Thông báo không khớp. Dự kiến: '{expected_notice}', nhưng thực tế: '{notice.text}'"
    print(f"Thông báo hiển thị và khớp với mong đợi: {expected_notice}")

    # Add a short wait to verify the changes or submission (if needed)
    time.sleep(5)

# bug: kiểm tra khi email được để trống
def test_new_account_email_empty(chrome_driver):
    # 1. Điều hướng tới trang chủ
    navigate_to_index_page(chrome_driver)

    # 2. Đăng nhập với tư cách SuperAdmin
    login_success_superAdmin(chrome_driver)

    # 3. Nhấn vào tab "Account"
    account_tab = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'tab-title') and contains(., 'Account')]"))
    )
    account_tab.click()

    # 4. Nhấn vào nút có biểu tượng "fa-circle-info"
    info_button = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//i[contains(@class, 'fa-regular') and contains(@class, 'fa-circle-info')]"))
    )
    info_button.click()

    # 5. Click the "New" button using JavaScript if standard click fails
    new_button = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'new-button') and @onclick=\"loadModalBoxByAjax('newAccount')\"]")
        )
    )
    chrome_driver.execute_script("arguments[0].click();", new_button)

    # 6. Fill out the account form
    # Fill username field
    username_field = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='username']"))
    )
    username_field.send_keys("lhp1")

    # Fill name field
    name_field = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='name']"))
    )
    name_field.send_keys("LHP")

    # Fill email field
    email_field = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='email']"))
    )
    email_field.send_keys("hieuphong144@gmail.com")

    # Fill phone number field
    phone_field = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='phoneNumber']"))
    )
    phone_field.send_keys("0326526898")

    # Fill password field
    password_field = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='password']"))
    )
    password_field.send_keys("Tatooboys123@")

    # Fill address field
    address_field = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='address']"))
    )
    address_field.send_keys("abc")

    # 7. Nhấn vào nút "Add" để tạo tài khoản mới
    add_button = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'edit-button') and @onclick=\"createNewAccount()\"]")
        )
    )
    chrome_driver.execute_script("arguments[0].click();", add_button)

    time.sleep(2)

    # Chờ cho thông báo hiển thị
    notice = WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.ID, "notice")))

    expected_notice = "Please, enter your email!"
    assert notice.is_displayed(), f"Thông báo không hiển thị. Dự kiến: {expected_notice}"
    assert notice.text == expected_notice, f"Thông báo không khớp. Dự kiến: '{expected_notice}', nhưng thực tế: '{notice.text}'"
    print(f"Thông báo hiển thị và khớp với mong đợi: {expected_notice}")

    # Add a short wait to verify the changes or submission (if needed)
    time.sleep(5)

# bug: kiểm tra khi address được để trống
def test_new_account_address_empty(chrome_driver):
    # 1. Điều hướng tới trang chủ
    navigate_to_index_page(chrome_driver)

    # 2. Đăng nhập với tư cách SuperAdmin
    login_success_superAdmin(chrome_driver)

    # 3. Nhấn vào tab "Account"
    account_tab = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'tab-title') and contains(., 'Account')]"))
    )
    account_tab.click()

    # 4. Nhấn vào nút có biểu tượng "fa-circle-info"
    info_button = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//i[contains(@class, 'fa-regular') and contains(@class, 'fa-circle-info')]"))
    )
    info_button.click()

    # 5. Click the "New" button using JavaScript if standard click fails
    new_button = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'new-button') and @onclick=\"loadModalBoxByAjax('newAccount')\"]")
        )
    )
    chrome_driver.execute_script("arguments[0].click();", new_button)

    # 6. Fill out the account form
    # Fill username field
    username_field = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='username']"))
    )
    username_field.send_keys("lhp2")

    # Fill name field
    name_field = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='name']"))
    )
    name_field.send_keys("LHP")

    # Fill email field
    email_field = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='email']"))
    )
    email_field.send_keys("hieuphong144@gmail.com")

    # Fill phone number field
    phone_field = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='phoneNumber']"))
    )
    phone_field.send_keys("0326526898")

    # Fill password field
    password_field = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='password']"))
    )
    password_field.send_keys("Tatooboys123@")

    # Fill address field
    address_field = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='address']"))
    )
    address_field.send_keys("abc")

    # 7. Nhấn vào nút "Add" để tạo tài khoản mới
    add_button = WebDriverWait(chrome_driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'edit-button') and @onclick=\"createNewAccount()\"]")
        )
    )
    chrome_driver.execute_script("arguments[0].click();", add_button)

    time.sleep(2)

    # Chờ cho thông báo hiển thị
    notice = WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.ID, "notice")))

    expected_notice = "Please, enter your address!"
    assert notice.is_displayed(), f"Thông báo không hiển thị. Dự kiến: {expected_notice}"
    assert notice.text == expected_notice, f"Thông báo không khớp. Dự kiến: '{expected_notice}', nhưng thực tế: '{notice.text}'"
    print(f"Thông báo hiển thị và khớp với mong đợi: {expected_notice}")

    # Add a short wait to verify the changes or submission (if needed)
    time.sleep(5)