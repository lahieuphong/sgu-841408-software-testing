from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.base_driver import chrome_driver
from pages.checkout import click_place_order_button
from tests.test_add_to_cart import test_add_to_cart_with_negative_number_qty, test_add_to_cart_with_empty_qty


# bug: checkout thành công với số lượng âm
def test_checkout_with_negative_quantity(chrome_driver):
    test_add_to_cart_with_negative_number_qty(chrome_driver)

    click_place_order_button(chrome_driver)

    # Chờ đợi modal thông báo xuất hiện (chờ tối đa 10 giây)
    WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "div.modal-info-placeholder div.modal-info:nth-child(2)"))
    )

    # Lấy nội dung thông báo trong modal
    modal_message = chrome_driver.find_element(By.CSS_SELECTOR,
                                               "div.modal-info-placeholder div.modal-info:nth-child(2)").text

    expected_message = "Your order failed!"  # Thông báo mong đợi

    # In ra thông báo trong modal để dễ dàng kiểm tra
    print(f"Modal message: '{modal_message}'")

    # Kiểm tra nếu thông báo trong modal khớp với mong đợi
    assert modal_message == expected_message, f"Thông báo không chính xác! Mong đợi: '{expected_message}', nhưng nhận được: '{modal_message}'."

# bug: checkout với số lượng trống nhưng không hiển thị thông báo lỗi
def test_checkout_with_empty_quantity(chrome_driver):
    # Thực hiện bước thêm sản phẩm vào giỏ hàng với số lượng trống
    test_add_to_cart_with_empty_qty(chrome_driver)

    # Nhấn nút "Place order"
    place_order_button = chrome_driver.find_element(By.CSS_SELECTOR, "div.totalprice-button button")
    place_order_button.click()  # Nhấn nút "Place order"

    # Lấy nội dung thông báo trong modal
    try:
        modal_message = chrome_driver.find_element(By.CSS_SELECTOR,
                                                   "div.modal-info-placeholder div.modal-info:nth-child(2)").text.strip()
    except Exception as e:
        modal_message = ""  # Nếu không có thông báo, gán chuỗi rỗng

    # In ra thông báo trong modal để dễ dàng kiểm tra
    print(f"Modal message: '{modal_message}'")

    # Đặt thông báo mong đợi
    expected_message = "Your order failed!"  # Thông báo mong đợi

    # Kiểm tra nếu thông báo trong modal khớp với mong đợi
    assert modal_message == expected_message, f"Thông báo không chính xác! Mong đợi: '{expected_message}', nhưng nhận được: '{modal_message}'."

    # Nếu không nhận được thông báo, in thêm thông báo lỗi để dễ dàng debug
    if not modal_message:
        print("Không có thông báo hiển thị trong modal!")