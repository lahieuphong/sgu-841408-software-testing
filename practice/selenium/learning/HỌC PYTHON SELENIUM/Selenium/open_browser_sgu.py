from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
import subprocess

# Đường dẫn tới thư mục profile nơi sẽ lưu dữ liệu người dùng
account_sgu = '/Users/lahieuphong/Documents/Selenium/account_sgu'

# Khởi chạy Chrome với lệnh và đường dẫn profile chỉ định (ẩn lỗi và stdout)
chrome_command = '/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome --user-data-dir=/Users/lahieuphong/Documents/Selenium/account_sgu --remote-debugging-port=8989'
# Chạy lệnh để mở Chrome với cấu hình từ terminal mà không hiển thị lỗi và thông báo
subprocess.Popen(chrome_command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Tạo tuỳ chọn Chrome, sử dụng profile đã lưu và thiết lập cổng debug
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-data-dir={account_sgu}")  # Chỉ định thư mục lưu profile
chrome_options.add_experimental_option('debuggerAddress', '127.0.0.1:8989')  # Kết nối tới cổng debug

# Khởi tạo WebDriver với các tuỳ chọn đã cấu hình
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://thongtindaotao.sgu.edu.vn')  # Điều hướng tới trang đăng nhập
sleep(2)  # Đợi một chút để trang tải

# Biến đếm số lần thử đăng nhập
case_number = 1
max_attempts = 5  # Đặt số lần thử tối đa là 5 lần

# Vòng lặp để thực hiện các thử nghiệm đăng nhập tối đa `max_attempts` lần
while case_number <= max_attempts:
    try:
        # Tìm và lấy đối tượng trường nhập liệu cho tên đăng nhập
        username_field = driver.find_element(By.NAME, "username")

        # Tìm và lấy đối tượng trường nhập liệu cho mật khẩu
        password_field = driver.find_element(By.NAME, "password")

        # Tìm và lấy đối tượng nút đăng nhập
        login_button = driver.find_element(By.XPATH,
                                           "/html/body/app-root/div/div/div/div[1]/div/div/div[2]/app-right/app-login/div/div[2]/div/div[4]/button")

        # In ra thông báo cho người dùng biết đang thử đăng nhập với số thứ tự case hiện tại
        print(f'Attempting login, Case: {case_number}')
        sleep(2)  # Tạm dừng 2 giây trước khi tiếp tục

        try:
            # Chờ cho tới khi một phần tử chỉ ra rằng đăng nhập thành công xuất hiện (nút đăng xuất chẳng hạn)
            success_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "/html/body/app-root/div/div/div/div[1]/div/div/div[2]/app-right/app-login/div/div[2]/div[2]/button"))
            )
            # Nếu đăng nhập thành công, in ra kết quả thành công cho case hiện tại và thoát khỏi vòng lặp
            print(f'Case {case_number}: pass')
            break  # Thoát khỏi vòng lặp nếu đăng nhập thành công

        except:
            # Nếu không tìm thấy phần tử xác nhận thành công, nghĩa là đăng nhập thất bại
            error_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                "/html/body/app-root/div/div/div/div[1]/div/div/div[2]/app-right/app-login/div/div[2]/div/div[3]/div"))
            )
            # In ra thông báo đăng nhập thất bại cho case hiện tại
            print(f'Case {case_number}: fail')
            case_number += 1  # Tăng số thứ tự case để thử lại lần sau

    except Exception as e:
        # Nếu có lỗi xảy ra, in ra lỗi và thoát khỏi vòng lặp
        print(f"Error: {e}")
        break

# Cuối cùng có thể đóng trình duyệt nếu cần (được comment ở đây)
# finally:
#     driver.quit()