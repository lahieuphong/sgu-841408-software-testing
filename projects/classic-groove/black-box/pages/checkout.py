from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Hàm để chuyển đổi chuỗi thành giá trị số (float) để so sánh
def convert_to_float(value: str) -> float:
    # Loại bỏ dấu '$' và chuyển thành float
    return float(value.replace("$", "").replace(",", "").strip())


# Nút Checkout (Place Order)
def click_place_order_button(chrome_driver):
    place_order_button = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.totalprice-button button"))
    )
    place_order_button.click()

    WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal-info-placeholder"))
    )


def check_order_processing_modal(chrome_driver):
    # Kiểm tra thông báo trong modal
    modal_message = chrome_driver.find_element(By.CSS_SELECTOR,
                                               "div.modal-info-placeholder div.modal-info:nth-child(2)").text
    expected_message = "Your order is being processed and shipped in shortly !"

    # Kiểm tra nếu thông báo xuất hiện
    assert modal_message == expected_message, f"Thông báo không chính xác! Mong đợi: '{expected_message}', nhưng nhận được: '{modal_message}'."
    # print("Your order is being processed and shipped in shortly !")