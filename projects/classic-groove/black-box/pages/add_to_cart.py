import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def add_product_to_cart_and_check_notice(chrome_driver):
    # Thêm sản phẩm vào giỏ hàng
    add_to_cart_button = chrome_driver.find_element(By.CSS_SELECTOR, "div.btn.add-to-cart-btn")
    add_to_cart_button.click()
    time.sleep(1)

    # Kiểm tra thông báo "Added to your Cart" hoặc "Album already exists in your cart!"
    check_cart_notice(chrome_driver)


def check_cart_notice(chrome_driver):
    try:
        # Chờ cho thông báo hiển thị
        notice = WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.ID, "notice")))

        # Kiểm tra thông báo 'Added to your Cart'
        if "Added to your Cart" in notice.text:
            expected_notice = "Added to your Cart"
            assert notice.is_displayed(), f"Thông báo không hiển thị. Dự kiến: {expected_notice}"
            assert notice.text == expected_notice, f"Thông báo không khớp. Dự kiến: '{expected_notice}', nhưng thực tế: '{notice.text}'"
            print(f"Thông báo hiển thị và khớp với mong đợi: {expected_notice}")

        # Kiểm tra thông báo 'Album already exists in your cart'
        elif "Album already exists in your cart!" in notice.text:
            expected_notice = "Album already exists in your cart!"
            assert notice.is_displayed(), "Thông báo 'Album already exists in your cart!' không hiển thị."
            print(f"Thông báo hiển thị và khớp với mong đợi: {expected_notice}")
            # Thoát testcase nếu sản phẩm đã có trong giỏ hàng
            return False  # Trả về False để thoát khỏi test case khi sản phẩm đã có trong giỏ hàng

        else:
            # Nếu không có thông báo nào hợp lệ, raise exception
            raise Exception(f"Thông báo không hợp lệ: {notice.text}")

        time.sleep(5)  # Đợi thêm 5 giây để xác nhận thông báo
        return True  # Trả về True nếu thông báo hợp lệ

    except Exception as e:
        print(f"Lỗi khi kiểm tra thông báo: {e}")
        return False  # Trả về False nếu có lỗi trong quá trình kiểm tra


def click_cart_icon(chrome_driver):
    cart_icon = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "i.fa-regular.fa-cart-shopping"))
    )
    actions = ActionChains(chrome_driver)
    actions.move_to_element(cart_icon).click().perform()


def click_checkbox(driver, checkbox_value):
    try:
        # Wait for the checkbox to be clickable
        checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f"input[type='checkbox'][value='{checkbox_value}']"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)

        # Wait a bit to ensure the page is fully settled
        WebDriverWait(driver, 2).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )

        # Check if it's already selected
        if not checkbox.is_selected():
            try:
                checkbox.click()
            except Exception as e:
                print(f"Direct click failed, using JavaScript for checkbox {checkbox_value}. Error: {e}")
                driver.execute_script("arguments[0].click();", checkbox)
    except Exception as e:
        print(f"Failed to interact with checkbox {checkbox_value}: {e}")