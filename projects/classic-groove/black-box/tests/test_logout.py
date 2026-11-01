from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.base_driver import chrome_driver
from pages.navigate import navigate_to_index_page
from pages.login import login_success_customer
from pages.logout import logout


# bug: don't show message when logging out
def test_logout_functionality(chrome_driver):
    navigate_to_index_page(chrome_driver)
    login_success_customer(chrome_driver)
    logout(chrome_driver)

    try:
        # Đợi thông báo xuất hiện sau khi logout
        logout_message = WebDriverWait(chrome_driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.notification"))
        )

        # Lấy nội dung của thông báo
        actual_message = logout_message.text.strip()
    except TimeoutException:
        actual_message = ""  # Nếu thông báo không xuất hiện, đặt chuỗi rỗng

    # Kiểm tra thông báo có khớp với kỳ vọng hay không
    expected_message = "Notice: Logout successful."
    assert actual_message == expected_message, f"Test Failed: Expected '{expected_message}', but got '{actual_message}'"