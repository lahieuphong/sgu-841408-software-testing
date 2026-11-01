from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

@app.route('/')
def index():
    # Cấu hình các tùy chọn cho trình duyệt
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Tùy chọn để chạy ở chế độ không hiển thị giao diện

    # Tạo đối tượng Service với webdriver_manager
    service = Service(ChromeDriverManager().install())

    # Khởi tạo trình điều khiển Chrome
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Mở trang web
    driver.get("https://vnexpress.net/")

    # Lấy tiêu đề trang
    title = driver.title

    # Tìm tất cả các phần tử theo CSS selector
    elements = driver.find_elements(By.CSS_SELECTOR, "article.item-news h3")
    texts = [el.text for el in elements]

    # Đóng trình duyệt
    driver.quit()

    # Trả về template với các biến
    return render_template('index.html', title=title, texts=texts)

if __name__ == '__main__':
    app.run(debug=True)