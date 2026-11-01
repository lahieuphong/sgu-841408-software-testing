import time
from selenium.webdriver.common.by import By
from utils.base_driver import chrome_driver
from pages.navigate import navigate_to_index_page
from pages.login import login_success_customer


#bug: không thay đổi được mật khẩu và lỗi mesage
def test_change_password(chrome_driver):
    print(f"\n")
    print(f"-" * 40)
    navigate_to_index_page(chrome_driver)
    login_success_customer(chrome_driver)
    print(f"-" * 40)

    # Nhấn vào biểu tượng người dùng
    user_icon = chrome_driver.find_element(By.CSS_SELECTOR, "i.fa-solid.fa-user")
    user_icon.click()
    time.sleep(1)  # Chờ một chút để form hiển thị

    # Nhập mật khẩu cũ
    old_password_input = chrome_driver.find_element(By.ID, "txtOldPassword")
    old_password_input.click()
    old_password_input.send_keys("Tatooboys123@")
    # in terminal
    old_password_value = old_password_input.get_attribute("value")
    print(f"OldPassword: {old_password_value}")

    # Nhập mật khẩu mới
    new_password_input = chrome_driver.find_element(By.ID, "txtNewPassword")
    new_password_input.click()
    new_password_input.send_keys("Tatooboys123@@@")
    # in terminal
    new_password_value = new_password_input.get_attribute("value")
    print(f"NewPassword: {new_password_value}")

    # Xác nhận mật khẩu mới
    confirm_new_password_input = chrome_driver.find_element(By.ID, "txtConfirmNewPassword")
    confirm_new_password_input.click()
    confirm_new_password_input.send_keys("Tatooboys123@@@")
    # in terminal
    confirm_password_value = confirm_new_password_input.get_attribute("value")
    print(f"ConfirmNewPassword: {confirm_password_value}")

    # Xác định nút "Save change" thứ hai bằng XPath
    save_change_button_password = chrome_driver.find_element(By.XPATH, "(//div[contains(@class, 'button-placeholder btnSave')])[2]")
    # Cuộn đến nút nếu nó không hiển thị
    chrome_driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", save_change_button_password)
    # Kiểm tra nút có hiển thị hay không
    assert save_change_button_password.is_displayed(), "Nút 'Save change' thứ hai không hiển thị!"

    # Nhấn vào nút
    save_change_button_password.click()
    print("Nhấn nút 'Save change'.")

    time.sleep(2)

    # Lấy nội dung thông báo trong notice
    notice = chrome_driver.find_element(By.ID, "notice").text.strip()
    expected_notice = "Password updated successfully!"  # Thông báo mong đợi
    # In ra thông báo trong notice để dễ dàng kiểm tra
    print(f"Modal message: '{notice}'")
    # Kiểm tra nếu thông báo trong notice khớp với mong đợi
    assert notice == expected_notice, f"Thông báo không chính xác! Mong đợi: '{expected_notice}', nhưng nhận được: '{notice}'."