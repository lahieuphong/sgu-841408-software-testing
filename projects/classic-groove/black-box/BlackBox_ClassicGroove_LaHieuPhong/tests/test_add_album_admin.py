import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.base_driver import chrome_driver
from pages.login import login_success_superAdmin, login_success_customer
from pages.navigate import navigate_to_index_page
from pages.add_album_admin import wait_for_clickable_element, click_element


def test_addAlbumAdmin(chrome_driver):
    # Navigate to the website
    navigate_to_index_page(chrome_driver)
    time.sleep(2)
    login_success_superAdmin(chrome_driver)

    # Navigate to product manager
    chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[2]').click()
    time.sleep(2)
    product_manager = wait_for_clickable_element(chrome_driver, (By.XPATH, '//*[@id="productManager"]/div[1]/div[1]/div'))
    click_element(chrome_driver, product_manager)

    # Wait for dropdown and select option
    WebDriverWait(chrome_driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="new-album"]/div/div[2]/div/div[3]/div[2]'))
    )
    select_option = chrome_driver.find_element(By.XPATH, '//*[@id="new-album"]/div/div[2]/div/div[3]/div[2]/select/option[3]')
    click_element(chrome_driver, select_option)

    chrome_driver.find_element(By.XPATH, '//*[@id="new-album"]/div/div[2]/div/div[2]/div[2]/input').send_keys("Mochiii")
    chrome_driver.find_element(By.XPATH, '//*[@id="new-album"]/div/div[2]/div/div[4]/div[2]/input').send_keys("Mochiii")
    chrome_driver.find_element(By.XPATH, '//*[@id="new-album"]/div/div[2]/div/div[6]/div[2]/input').send_keys("300")
    chrome_driver.find_element(By.XPATH, '//*[@id="new-album"]/div/div[2]/div/div[8]/div[2]/textarea').send_keys(
        "ACV Entertainment")
    # Wait for the button to be clickable and click it
    add_song_button = wait_for_clickable_element(chrome_driver, (By.XPATH, '//*[@id="new-album"]/div/div[3]/div[3]/input[2]'))
    click_element(chrome_driver, add_song_button)
    chrome_driver.find_element(By.XPATH, '//*[@id="my-input"]').send_keys("26-Cánh Hoa Héo Tàn (Remix)")
    chrome_driver.find_element(By.XPATH, '//*[@id="add_exist_song"]/div/div[2]/input[1]').click()
    chrome_driver.find_element(By.XPATH, '//*[@id="new-album"]/div/div[4]/div[2]/div[2]').click()

    chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[2]').click()
    time.sleep(2)

    albums = chrome_driver.find_elements(By.CLASS_NAME, 'item')
    album_found = False

    print(f"\nALBUM NAME: ")

    for i in range(0, len(albums), 8):
        album_name = albums[i + 2].text.strip()
        artist_name = albums[i + 3].text.strip()
        print(album_name)

        if album_name == "Mochiii" and artist_name == "Mochiii":
            album_found = True
            break

    assert album_found, f"Album name 'Mochiii' by artist 'Mochiii' not found in the list."

    chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div').click()
    time.sleep(2)

    chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[1]/div[2]/div[2]').click()
    time.sleep(2)

    login = chrome_driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div[1]/div[1]/input')
    login.click()
    time.sleep(2)

    login_success_customer(chrome_driver)
    time.sleep(2)

    chrome_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    print("-" * 40)

    def check_album_and_artist():
        # Tìm tất cả các album trong grid
        albums = chrome_driver.find_elements(By.CLASS_NAME, "grid-item")  # Đảm bảo driver là đối tượng WebDriver

        # Kiểm tra tên album và nghệ sĩ
        for album in albums:
            album_name = album.find_element(By.CLASS_NAME, "title").text.strip()
            artist_name = album.find_element(By.CLASS_NAME, "artist").text.strip()

            if album_name == "Mochiii" and artist_name == "Mochiii":
                print("Album Mochiii và nghệ sĩ Mochiii đã được tìm thấy!")
                return True
        return False

    while True:
        if check_album_and_artist():
            break

        try:
            load_more_button = chrome_driver.find_element(By.XPATH, '//*[@id="home"]/div[3]/div/div[3]')
            load_more_button.click()
            time.sleep(2)
        except Exception as e:
            print("Không thể click để tải thêm, thoát khỏi vòng lặp.")
            break