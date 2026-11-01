import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.base_driver import chrome_driver
from pages.login import login_success_customer
from pages.search import search_and_select_product, clear_search_input
from pages.navigate import navigate_to_index_page
from pages.checkout import click_place_order_button
from pages.add_to_cart import add_product_to_cart_and_check_notice, click_cart_icon, click_checkbox


def test_add_to_cart_1_product(chrome_driver):
    print(f"\nADD 1 PRODUCT:")
    print(f"-" * 40)

    navigate_to_index_page(chrome_driver)

    login_success_customer(chrome_driver)
    print(f"-" * 30)

    # 1. Tìm kiếm & chọn sản phẩm "Beleive"
    search_and_select_product(chrome_driver, "Beleive")

    product_details_div = chrome_driver.find_element(By.CSS_SELECTOR, "div.right")
    title = product_details_div.find_element(By.CSS_SELECTOR, "p.title").text
    price = product_details_div.find_element(By.CSS_SELECTOR, "h2.price").text.replace('$', '').strip()
    print("Title:", title)
    print("Price: $", price)

    # 2. Thêm sản phẩm vào giỏ hàng & Kiểm tra thông báo "Added to your Cart" hoặc "Album already exists in your cart!"
    add_product_to_cart_and_check_notice(chrome_driver)

    # 3. Nhấn vào biểu tượng giỏ hàng (cart icon)
    click_cart_icon(chrome_driver)

    # 4. Tương tác với ô nhập số lượng (quantity input)
    quantity_input = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, f"input.quantity-info[onchange*='changeQuantity(7,0,this)']"))
    )

    # Clear giá trị trong ô nhập số lượng
    quantity_input.clear()

    # 5. Kiểm tra thông báo "Added to your Cart" khi Clear ô nhập số lượng
    WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.ID, "notice")))
    notice = chrome_driver.find_element(By.ID, "notice")
    assert notice.is_displayed(), "Thông báo ' Quantity must not be empty!' không hiển thị."
    # print("Quantity must not be empty!'")

    # 6. Nhập số lượng random từ 1 đến 99
    random_quantity = random.randint(1, 99)
    quantity_input.send_keys(str(random_quantity))
    print(f"Đã nhập số lượng: {random_quantity}")

    # 7. Nhấn vào checkbox
    click_checkbox(chrome_driver, "7")

    time.sleep(5)


def test_add_to_cart_multiple_products(chrome_driver):
    print(f"\nADD MULTIPLE PRODUCTS:")
    print(f"-" * 40)

    navigate_to_index_page(chrome_driver)

    login_success_customer(chrome_driver)
    print(f"-" * 30)

    # THÊM SẢN PHẨM 1
    print(f"ADD PRODUCT 1:")
    # 1. Tìm kiếm & chọn sản phẩm "Beleive"
    search_and_select_product(chrome_driver, "Beleive")

    product_details_div = chrome_driver.find_element(By.CSS_SELECTOR, "div.right")
    title = product_details_div.find_element(By.CSS_SELECTOR, "p.title").text
    price = product_details_div.find_element(By.CSS_SELECTOR, "h2.price").text.replace('$', '').strip()
    print("Title:", title)
    print("Price: $", price)

    # 2. Thêm sản phẩm vào giỏ hàng & Kiểm tra thông báo "Added to your Cart" hoặc "Album already exists in your cart!"
    add_product_to_cart_and_check_notice(chrome_driver)

    # 3. Nhấn vào biểu tượng giỏ hàng (cart icon)
    click_cart_icon(chrome_driver)

    # 4. Tương tác với ô nhập số lượng (quantity input)
    quantity_input_7 = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, f"input.quantity-info[onchange*='changeQuantity(7,0,this)']"))
    )

    # Clear giá trị trong ô nhập số lượng
    quantity_input_7.clear()

    # 5. Kiểm tra thông báo "Added to your Cart" khi Clear ô nhập số lượng
    WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.ID, "notice")))
    notice = chrome_driver.find_element(By.ID, "notice")
    assert notice.is_displayed(), "Thông báo ' Quantity must not be empty!' không hiển thị."
    # print("Quantity must not be empty!'")

    # 6. Nhập số lượng random từ 1 đến 99
    random_quantity_7 = random.randint(1, 99)
    quantity_input_7.send_keys(str(random_quantity_7))  # Chuyển đổi số lượng sang chuỗi trước khi nhập
    print(f"Đã nhập số lượng: {random_quantity_7}")


    clear_search_input(chrome_driver)


    # THÊM SẢN PHẨM 2
    print(f"\nADD PRODUCT 2:")
    # 1. Tìm kiếm & chọn sản phẩm "J97"
    search_and_select_product(chrome_driver, "J97")

    product_details_div = chrome_driver.find_element(By.CSS_SELECTOR, "div.right")
    title = product_details_div.find_element(By.CSS_SELECTOR, "p.title").text
    price = product_details_div.find_element(By.CSS_SELECTOR, "h2.price").text.replace('$', '').strip()
    print("Title:", title)
    print("Price: $", price)

    # 2. Thêm sản phẩm vào giỏ hàng & Kiểm tra thông báo "Added to your Cart" hoặc "Album already exists in your cart!"
    add_product_to_cart_and_check_notice(chrome_driver)

    # 3. Nhấn vào biểu tượng giỏ hàng (cart icon)
    click_cart_icon(chrome_driver)

    # 4. Tương tác với ô nhập số lượng (quantity input)
    quantity_input_12 = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, f"input.quantity-info[onchange*='changeQuantity(12,0,this)']"))
    )

    # Clear giá trị trong ô nhập số lượng
    quantity_input_12.clear()

    # 5. Kiểm tra thông báo "Added to your Cart" khi Clear ô nhập số lượng
    WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.ID, "notice")))
    notice = chrome_driver.find_element(By.ID, "notice")
    assert notice.is_displayed(), "Thông báo ' Quantity must not be empty!' không hiển thị."
    # print("Quantity must not be empty!'")

    # 6. Nhập số lượng random từ 1 đến 99
    random_quantity_12 = random.randint(1, 99)
    quantity_input_12.send_keys(str(random_quantity_12))  # Chuyển đổi số lượng sang chuỗi trước khi nhập
    print(f"Đã nhập số lượng: {random_quantity_12}")

    # Click checkboxes
    click_checkbox(chrome_driver, "7")
    chrome_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    click_checkbox(chrome_driver, "12")

    time.sleep(5)

    click_place_order_button(chrome_driver)


def test_add_to_cart_with_empty_qty(chrome_driver):
    print(f"\n")
    print(f"-" * 40)

    navigate_to_index_page(chrome_driver)

    login_success_customer(chrome_driver)
    print(f"-" * 40)

    # 1. Tìm kiếm & chọn sản phẩm "Beleive"
    search_and_select_product(chrome_driver, "Beleive")

    product_details_div = chrome_driver.find_element(By.CSS_SELECTOR, "div.right")
    title = product_details_div.find_element(By.CSS_SELECTOR, "p.title").text
    print("Title:", title)

    # 2. Thêm sản phẩm vào giỏ hàng & Kiểm tra thông báo "Added to your Cart" hoặc "Album already exists in your cart!"
    add_product_to_cart_and_check_notice(chrome_driver)

    # 3. Nhấn vào biểu tượng giỏ hàng (cart icon)
    click_cart_icon(chrome_driver)

    # 4. Tương tác với ô nhập số lượng (quantity input)
    quantity_input = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, f"input.quantity-info[onchange*='changeQuantity(7,0,this)']"))
    )

    # Clear giá trị trong ô nhập số lượng
    quantity_input.clear()

    click_checkbox(chrome_driver, "7")

    WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.ID, "notice")))
    notice = chrome_driver.find_element(By.ID, "notice")

    expected_notice = "Quantity must not be empty!"  # Thông báo mong đợi

    # Lọc thông báo chỉ chứa 'Quantity must not be empty!'
    notice_text = notice.text.strip().split('\n')[-1]  # Lấy phần cuối của thông báo (sau khi đã loại bỏ phần trước)

    # So sánh nội dung thông báo
    assert notice.is_displayed(), f"Thông báo không hiển thị. Dự kiến: {expected_notice}"
    assert notice_text == expected_notice, f"Thông báo không khớp. Dự kiến: '{expected_notice}', nhưng thực tế: '{notice_text}'"

    print(f"Thông báo hiển thị và khớp với mong đợi: {expected_notice}")

    time.sleep(5)


def test_add_to_cart_with_zero_qty(chrome_driver):
    print(f"\n")
    print(f"-" * 40)

    navigate_to_index_page(chrome_driver)

    login_success_customer(chrome_driver)
    print(f"-" * 30)

    # 1. Tìm kiếm & chọn sản phẩm "Beleive"
    search_and_select_product(chrome_driver, "Beleive")

    product_details_div = chrome_driver.find_element(By.CSS_SELECTOR, "div.right")
    title = product_details_div.find_element(By.CSS_SELECTOR, "p.title").text
    print("Title:", title)

    # 2. Thêm sản phẩm vào giỏ hàng & Kiểm tra thông báo "Added to your Cart" hoặc "Album already exists in your cart!"
    add_product_to_cart_and_check_notice(chrome_driver)

    # 3. Nhấn vào biểu tượng giỏ hàng (cart icon)
    click_cart_icon(chrome_driver)

    # 4. Tương tác với ô nhập số lượng (quantity input)
    quantity_input = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, f"input.quantity-info[onchange*='changeQuantity(7,0,this)']"))
    )

    # Clear giá trị trong ô nhập số lượng
    quantity_input.clear()

    # 5. Kiểm tra thông báo "Quantity must not be empty!" khi Clear ô nhập số lượng
    WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.ID, "notice")))
    notice = chrome_driver.find_element(By.ID, "notice")

    expected_notice = "Quantity must not be empty!"  # Thông báo mong đợi

    # Lọc thông báo chỉ chứa 'Quantity must not be empty!'
    notice_text = notice.text.strip().split('\n')[-1]  # Lấy phần cuối của thông báo (sau khi đã loại bỏ phần trước)

    # So sánh nội dung thông báo
    assert notice.is_displayed(), f"Thông báo không hiển thị. Dự kiến: {expected_notice}"
    assert notice_text == expected_notice, f"Thông báo không khớp. Dự kiến: '{expected_notice}', nhưng thực tế: '{notice_text}'"

    print(f"Thông báo hiển thị và khớp với mong đợi: {expected_notice}")


    # 6. Nhập số lượng 0
    quantity_input.send_keys('0')
    print(f"Đã nhập số lượng: {quantity_input.get_attribute('value')}")

    click_checkbox(chrome_driver, "7")

    # Kiểm tra thông báo "Min is 1!" khi nhập số lượng 0
    WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.ID, "notice")))
    notice = chrome_driver.find_element(By.ID, "notice")

    expected_notice = "Min is 1"  # Thông báo mong đợi

    # Lọc thông báo chỉ chứa 'Min is 1!'
    notice_text = notice.text.strip().split('\n')[-1]  # Lấy phần trước cuối cùng (là thông báo về số lượng tối thiểu)

    # So sánh nội dung thông báo
    assert notice.is_displayed(), f"Thông báo không hiển thị. Dự kiến: {expected_notice}"
    assert notice_text == expected_notice, f"Thông báo không khớp. Dự kiến: '{expected_notice}', nhưng thực tế: '{notice_text}'"

    print(f"Thông báo hiển thị và khớp với mong đợi: {expected_notice}")

    time.sleep(5)


def test_add_to_cart_with_negative_number_qty(chrome_driver):
    print(f"\n")
    print(f"-" * 40)

    navigate_to_index_page(chrome_driver)

    login_success_customer(chrome_driver)
    print(f"-" * 30)

    # 1. Tìm kiếm & chọn sản phẩm "Beleive"
    search_and_select_product(chrome_driver, "Beleive")

    product_details_div = chrome_driver.find_element(By.CSS_SELECTOR, "div.right")
    title = product_details_div.find_element(By.CSS_SELECTOR, "p.title").text
    price = product_details_div.find_element(By.CSS_SELECTOR, "h2.price").text.replace('$', '').strip()
    print("Title:", title)
    print("Price: $", price)

    # 2. Thêm sản phẩm vào giỏ hàng & Kiểm tra thông báo "Added to your Cart" hoặc "Album already exists in your cart!"
    add_product_to_cart_and_check_notice(chrome_driver)

    # 3. Nhấn vào biểu tượng giỏ hàng (cart icon)
    click_cart_icon(chrome_driver)

    # 4. Tương tác với ô nhập số lượng (quantity input)
    quantity_input = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, f"input.quantity-info[onchange*='changeQuantity(7,0,this)']"))
    )

    # Clear giá trị trong ô nhập số lượng
    quantity_input.clear()


    # 5. Kiểm tra thông báo "Quantity must not be empty!" khi Clear ô nhập số lượng
    WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.ID, "notice")))
    notice = chrome_driver.find_element(By.ID, "notice")

    expected_notice = "Quantity must not be empty!"  # Thông báo mong đợi

    # Lọc thông báo chỉ chứa 'Quantity must not be empty!'
    notice_text = notice.text.strip().split('\n')[-1]  # Lấy phần cuối của thông báo (sau khi đã loại bỏ phần trước)

    # So sánh nội dung thông báo
    assert notice.is_displayed(), f"Thông báo không hiển thị. Dự kiến: {expected_notice}"
    assert notice_text == expected_notice, f"Thông báo không khớp. Dự kiến: '{expected_notice}', nhưng thực tế: '{notice_text}'"

    print(f"Thông báo hiển thị và khớp với mong đợi: {expected_notice}")


    # 6. Nhập số lượng -1
    quantity_input.send_keys('-1')
    print(f"Đã nhập số lượng: {quantity_input.get_attribute('value')}")

    click_checkbox(chrome_driver, "7")

    # Kiểm tra thông báo "Min is 1!" khi nhập số lượng 0
    WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.ID, "notice")))
    notice = chrome_driver.find_element(By.ID, "notice")

    expected_notice = "quantity must be a number!"  # Thông báo mong đợi

    # Lọc thông báo chỉ chứa 'Min is 1!'
    notice_text = notice.text.strip().split('\n')[-1]  # Lấy phần trước cuối cùng (là thông báo về số lượng tối thiểu)

    # So sánh nội dung thông báo
    assert notice.is_displayed(), f"Thông báo không hiển thị. Dự kiến: {expected_notice}"
    assert notice_text == expected_notice, f"Thông báo không khớp. Dự kiến: '{expected_notice}', nhưng thực tế: '{notice_text}'"

    print(f"Thông báo hiển thị và khớp với mong đợi: {expected_notice}")

    time.sleep(5)


def test_add_to_cart_with_max_qty(chrome_driver):
    print(f"\n")
    print(f"-" * 40)

    navigate_to_index_page(chrome_driver)

    login_success_customer(chrome_driver)
    print(f"-" * 30)

    # 1. Tìm kiếm & chọn sản phẩm "Beleive"
    search_and_select_product(chrome_driver, "Beleive")

    product_details_div = chrome_driver.find_element(By.CSS_SELECTOR, "div.right")
    title = product_details_div.find_element(By.CSS_SELECTOR, "p.title").text
    print("Title:", title)

    # 2. Thêm sản phẩm vào giỏ hàng & Kiểm tra thông báo "Added to your Cart" hoặc "Album already exists in your cart!"
    add_product_to_cart_and_check_notice(chrome_driver)

    # 3. Nhấn vào biểu tượng giỏ hàng (cart icon)
    click_cart_icon(chrome_driver)

    # 4. Tương tác với ô nhập số lượng (quantity input)
    quantity_input = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, f"input.quantity-info[onchange*='changeQuantity(7,0,this)']"))
    )

    # Clear giá trị trong ô nhập số lượng
    quantity_input.clear()


    # 5. Kiểm tra thông báo "Quantity must not be empty!" khi Clear ô nhập số lượng
    WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.ID, "notice")))
    notice = chrome_driver.find_element(By.ID, "notice")

    expected_notice = "Quantity must not be empty!"  # Thông báo mong đợi

    # Lọc thông báo chỉ chứa 'Quantity must not be empty!'
    notice_text = notice.text.strip().split('\n')[-1]  # Lấy phần cuối của thông báo (sau khi đã loại bỏ phần trước)

    # So sánh nội dung thông báo
    assert notice.is_displayed(), f"Thông báo không hiển thị. Dự kiến: {expected_notice}"
    assert notice_text == expected_notice, f"Thông báo không khớp. Dự kiến: '{expected_notice}', nhưng thực tế: '{notice_text}'"

    print(f"Thông báo hiển thị và khớp với mong đợi: {expected_notice}")


    # 6. Nhập số lượng 100
    quantity_input.send_keys('100')
    print(f"Đã nhập số lượng: {quantity_input.get_attribute('value')}")

    click_checkbox(chrome_driver, "7")

    # Kiểm tra thông báo "Min is 1!" khi nhập số lượng 0
    WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.ID, "notice")))
    notice = chrome_driver.find_element(By.ID, "notice")

    expected_notice = "Max is 99"  # Thông báo mong đợi

    # Lọc thông báo chỉ chứa 'Min is 1!'
    notice_text = notice.text.strip().split('\n')[-1]  # Lấy phần trước cuối cùng (là thông báo về số lượng tối thiểu)

    # So sánh nội dung thông báo
    assert notice.is_displayed(), f"Thông báo không hiển thị. Dự kiến: {expected_notice}"
    assert notice_text == expected_notice, f"Thông báo không khớp. Dự kiến: '{expected_notice}', nhưng thực tế: '{notice_text}'"

    print(f"Thông báo hiển thị và khớp với mong đợi: {expected_notice}")

    time.sleep(5)