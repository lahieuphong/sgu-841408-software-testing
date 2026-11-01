from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def search_video(browser):
    # Đợi một khoảng thời gian trước khi tìm kiếm hộp tìm kiếm
    time.sleep(2)

    search_box = browser.find_element(By.CSS_SELECTOR, "input#search")
    search_box.send_keys('CHẲNG GÌ ĐẸP ĐẼ TRÊN ĐỜI MÃI - KHANG VIỆT | OFFICIAL MUSIC VIDEO')

    # Đợi thêm một khoảng thời gian trước khi nhấp vào nút tìm kiếm
    time.sleep(2)

    search_button = browser.find_element(By.ID, "search-icon-legacy")
    search_button.click()

    # Đợi thêm một khoảng thời gian trước khi nhấp vào video đầu tiên
    time.sleep(2)

    first_video = browser.find_element(By.XPATH, "//ytd-video-renderer[1]//a[@id='thumbnail']")
    first_video.click()

    # Chờ 6 giây rồi cố gắng bỏ qua quảng cáo nếu có
    time.sleep(6)
    try:
        skip_ads_button = browser.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[21]/div/div[3]/div/button")
        skip_ads_button.click()
    except Exception as e:
        print("Không tìm thấy nút bỏ qua quảng cáo:", e)

    # Chờ video phát trong một thời gian rồi thoát
    time.sleep(200)

if __name__ == '__main__':
    chrome_options = Options()
    browser = webdriver.Chrome(options=chrome_options)

    try:
        # Mở YouTube
        browser.get("https://www.youtube.com/")
        time.sleep(2)

        # Gọi hàm tìm kiếm video
        search_video(browser)
    finally:
        # Đóng trình duyệt sau khi hoàn tất
        browser.quit()
