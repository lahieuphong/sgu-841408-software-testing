import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.base_driver import chrome_driver
from pages.login import login_success_customer, login_success_superAdmin
from pages.search import search_and_select_product, clear_search_input
from pages.logout import logout
from pages.navigate import navigate_to_index_page
from pages.checkout import convert_to_float, click_place_order_button, check_order_processing_modal
from pages.add_to_cart import add_product_to_cart_and_check_notice, click_cart_icon


def test_compare_checkout_total_with_order_total(chrome_driver):
    print(f"\nADD TO CART & CHECKOUT - INDEX PAGE:")
    print(f"-" * 40)

    navigate_to_index_page(chrome_driver)

    login_success_customer(chrome_driver)
    print(f"-" * 30)

    # 1. Tìm kiếm & chọn sản phẩm "J97"
    search_and_select_product(chrome_driver, "J97")

    # 2. Thêm sản phẩm vào giỏ hàng & Kiểm tra thông báo "Added to your Cart" hoặc "Album already exists in your cart!"
    add_product_to_cart_and_check_notice(chrome_driver)

    # 3. Nhấn vào biểu tượng giỏ hàng (cart icon)
    click_cart_icon(chrome_driver)

    # 4. Tương tác với ô nhập số lượng (quantity input)
    quantity_input = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input.quantity-info"))
    )

    # Clear giá trị trong ô nhập số lượng
    quantity_input.clear()

    # 5. Kiểm tra thông báo "Added to your Cart"
    WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.ID, "notice")))
    notice = chrome_driver.find_element(By.ID, "notice")
    assert notice.is_displayed(), "Thông báo ' Quantity must not be empty!' không hiển thị."
    # print("Quantity must not be empty!'")

    # 6. Nhập số lượng random từ 1 đến 99
    random_quantity = random.randint(1, 99)
    quantity_input.send_keys(str(random_quantity))  # Chuyển đổi số lượng sang chuỗi trước khi nhập
    print(f"Đã nhập số lượng: {random_quantity}")

    # 7. Nhấn vào checkbox
    checkbox = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='checkbox'][value='12']"))
    )
    checkbox.click()

    time.sleep(5)


    #### Print the content of the checkout section after clicking the checkbox
    checkout_container = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.totalprice-placeholder"))
    )

    # Extract relevant details from the checkout section
    subtotal = checkout_container.find_element(By.CSS_SELECTOR, ".subtotal").text
    shipping = checkout_container.find_element(By.CSS_SELECTOR, ".shipping").text
    discount = checkout_container.find_element(By.CSS_SELECTOR, ".discount").text
    total_final = checkout_container.find_element(By.CSS_SELECTOR, ".total-final").text

    # Print the extracted details
    print(f"\nSubtotal: {subtotal}")
    print(f"Shipping: {shipping}")
    print(f"Discount: {discount}")
    print(f"Total: {total_final}")
    ##############################################################################

    # 8. Nhấn vào nút "Place order"
    click_place_order_button(chrome_driver)

    # 9. Kiểm tra modal thông báo "Order is being processed"
    check_order_processing_modal(chrome_driver)

    time.sleep(5)

    logout(chrome_driver)

    time.sleep(3)

    print(f"\n")
    login_success_superAdmin(chrome_driver)
    print(f"-" * 30)

    print("\nORDER - ADMIN PAGE:")
    print(f"-" * 40)

    # 1. Click vào tab "Order" sau khi đăng nhập thành công
    order_tab = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'tab-title') and contains(., 'Order')]"))
    )
    order_tab.click()

    time.sleep(5)

    # 2. Lấy tất cả các orders
    orders = chrome_driver.find_elements(By.CSS_SELECTOR, "div.list div.placeholder")

    #### In ra thông tin của mỗi đơn hàng
    if orders:  # Kiểm tra xem có đơn hàng không
        last_order = orders[-1]  # Lấy đơn hàng cuối cùng
        order_no = last_order.find_elements(By.CSS_SELECTOR, "div.item")[0].text
        order_id = last_order.find_elements(By.CSS_SELECTOR, "div.item")[1].text
        account_id = last_order.find_elements(By.CSS_SELECTOR, "div.item")[2].text
        order_date = last_order.find_elements(By.CSS_SELECTOR, "div.item")[3].text
        total_price = last_order.find_elements(By.CSS_SELECTOR, "div.item")[4].text
        discount = last_order.find_elements(By.CSS_SELECTOR, "div.item")[5].text
        status = last_order.find_elements(By.CSS_SELECTOR, "div.item")[6].text

        print(f"\nOrder No: {order_no}")
        print(f"Order ID: {order_id}")
        print(f"Account ID: {account_id}")
        print(f"Date of Order: {order_date}")
        print(f"Total Price: {total_price}")
        print(f"Discount: {discount}")
        print(f"Status: {status}")
        print("-" * 50)

    ##############################################################################

        # Chuyển đổi cả hai giá trị
        checkout_total = convert_to_float(total_final)
        order_total = convert_to_float(total_price)

        # So sánh các giá trị
        if checkout_total == order_total:
            print(f"Checkout total: {checkout_total} = Order total: {order_total}")
            print("Giá trị tổng (Total) khớp nhau.")
        else:
            print(f"Giá trị tổng không khớp! Checkout total: {checkout_total}, Order total: {order_total}")


def test_compare_checkout_subtotal_vs_manual_calculation(chrome_driver):
    print(f"\n")
    print(f"-" * 30)
    navigate_to_index_page(chrome_driver)
    login_success_customer(chrome_driver)
    print(f"-" * 30)

    # THÊM SẢN PHẨM 1
    print(f"ADD PRODUCT 1:")
    # Tìm kiếm & chọn sản phẩm dựa trên tên
    search_and_select_product(chrome_driver, "Evo Sessions")

    # Lấy thông tin chi tiết của sản phẩm
    product_details_div = chrome_driver.find_element(By.CSS_SELECTOR, "div.right")

    # Trích xuất các phần tử cần thiết và in chúng ra
    title = product_details_div.find_element(By.CSS_SELECTOR, "p.title").text
    sub_title = product_details_div.find_element(By.CSS_SELECTOR, "p.sub-title").text
    price_1 = product_details_div.find_element(By.CSS_SELECTOR, "h2.price").text.replace('$', '').strip()

    # In ra các thông tin chi tiết vào terminal
    print("Title:", title)
    print("Sub-title:", sub_title)
    print("Price: $", price_1)

    # Chuyển đổi giá trị price_1 thành float
    price_1 = float(price_1)

    # Thêm sản phẩm vào giỏ hàng & Kiểm tra thông báo
    add_product_to_cart_and_check_notice(chrome_driver)

    # Nhấn vào biểu tượng giỏ hàng (cart icon)
    click_cart_icon(chrome_driver)

    time.sleep(5)

    # Tìm ô nhập số lượng (quantity input) của sản phẩm
    quantity_input_1 = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, f"input.quantity-info[onchange*='changeQuantity(1,0,this)']"))
    )

    # Clear giá trị trong ô nhập số lượng
    quantity_input_1.clear()

    # Kiểm tra thông báo "Added to your Cart" khi Clear ô nhập số lượng
    WebDriverWait(chrome_driver, 10).until(EC.visibility_of_element_located((By.ID, "notice")))
    notice = chrome_driver.find_element(By.ID, "notice")
    assert notice.is_displayed(), "Thông báo ' Quantity must not be empty!' không hiển thị."

    # Nhập số lượng random từ 1 đến 99
    random_quantity_1 = random.randint(1, 99)
    quantity_input_1.send_keys(str(random_quantity_1))  # Chuyển đổi số lượng sang chuỗi trước khi nhập
    print(f"Đã nhập số lượng: {random_quantity_1}")


    clear_search_input(chrome_driver)


    # THÊM SẢN PHẨM 2
    print(f"ADD PRODUCT 2:")
    search_and_select_product(chrome_driver, "Dawn FM")

    # Lấy thông tin chi tiết của sản phẩm
    product_details_div = chrome_driver.find_element(By.CSS_SELECTOR, "div.right")

    # Trích xuất các phần tử cần thiết và in chúng ra
    title = product_details_div.find_element(By.CSS_SELECTOR, "p.title").text
    sub_title = product_details_div.find_element(By.CSS_SELECTOR, "p.sub-title").text
    price_2 = product_details_div.find_element(By.CSS_SELECTOR, "h2.price").text.replace('$', '').strip()

    # In ra các thông tin chi tiết vào terminal
    print("Title:", title)
    print("Sub-title:", sub_title)
    print("Price: $", price_2)

    # Chuyển đổi giá trị price_2 thành float
    price_2 = float(price_2)

    # Thêm sản phẩm vào giỏ hàng & Kiểm tra thông báo
    add_product_to_cart_and_check_notice(chrome_driver)

    # Nhấn vào biểu tượng giỏ hàng (cart icon)
    click_cart_icon(chrome_driver)

    time.sleep(5)

    # Tìm ô nhập số lượng (quantity input) của sản phẩm
    quantity_input_5 = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, f"input.quantity-info[onchange*='changeQuantity(5,0,this)']"))
    )

    # Clear giá trị trong ô nhập số lượng
    quantity_input_5.clear()

    # Nhập số lượng random từ 1 đến 99
    random_quantity_5 = random.randint(1, 99)
    quantity_input_5.send_keys(str(random_quantity_5))  # Chuyển đổi số lượng sang chuỗi trước khi nhập
    print(f"Đã nhập số lượng: {random_quantity_5}")

    # Nhấn checkbox của 2 sản phẩm trên
    checkbox_1 = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='checkbox'][value='1']"))
    )
    checkbox_1.click()

    time.sleep(2)

    checkbox_5 = WebDriverWait(chrome_driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='checkbox'][value='5']"))
    )
    checkbox_5.click()

    time.sleep(5)

    print(f"\nCHECKOUT PAGE:")
    #### Print the content of the checkout section after clicking the checkbox
    checkout_container = WebDriverWait(chrome_driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.totalprice-placeholder"))
    )

    # Extract relevant details from the checkout section
    subtotal = checkout_container.find_element(By.CSS_SELECTOR, ".subtotal").text
    shipping = checkout_container.find_element(By.CSS_SELECTOR, ".shipping").text
    discount = checkout_container.find_element(By.CSS_SELECTOR, ".discount").text
    total_final = checkout_container.find_element(By.CSS_SELECTOR, ".total-final").text

    # Print the extracted details
    print(f"Subtotal: {subtotal}")
    print(f"Shipping: {shipping}")
    print(f"Discount: {discount}")
    print(f"Total: {total_final}")

    print(f"-"*40)
    # Tính tổng thủ công (manual total)
    manual_total = (price_1 * random_quantity_1) + (price_2 * random_quantity_5)
    print(f"Manual Total: ${price_1:.2f} * ${random_quantity_1} + ${price_2:.2f} * ${random_quantity_5} = ${manual_total:.2f}")

    # Chuyển đổi Subtotal từ string thành số
    subtotal_value = float(subtotal.replace('$', '').strip())

    # So sánh manual_total với Subtotal
    if abs(manual_total - subtotal_value) < 0.01:  # Tolerance để tránh lỗi số học nhỏ
        print(f" ==> 'Subtotal': ${subtotal_value:.2f} matches with the 'Manual total': ${manual_total:.2f}")
    else:
        print(f" ==> Subtotal mismatch! Checkout subtotal: ${subtotal_value:.2f}, Manual total: ${manual_total:.2f}")

    click_place_order_button(chrome_driver)