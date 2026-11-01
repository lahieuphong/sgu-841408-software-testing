import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    # Khởi tạo trình duyệt
    driver = webdriver.Chrome()  # Đảm bảo đã cài đặt đúng ChromeDriver
    driver.get("https://playtictactoe.org/")  # Mở trang Tic-Tac-Toe
    yield driver
    driver.quit()  # Đóng trình duyệt sau khi kiểm thử

def test_player1_wins_player2_loses(browser):
    # Chuyển sang chế độ 2 người chơi
    mode_button = browser.find_element(By.CLASS_NAME, "swap")
    mode_button.click()

    # Lấy điểm số ban đầu của Player 1 và Player 2
    player1_score_initial = int(browser.find_element(By.CSS_SELECTOR, ".player1 .score").text)
    player2_score_initial = int(browser.find_element(By.CSS_SELECTOR, ".player2 .score").text)

    # Lấy các ô vuông trong bảng
    squares = browser.find_elements(By.CLASS_NAME, "square")

    # Player 1 thắng theo hàng trên cùng
    moves = [0, 3, 1, 4, 2]  # Player 1: 0, 1, 2; Player 2: 3, 4
    for move in moves:
        squares[move].click()
        time.sleep(1)

    # Lấy điểm số sau trận đấu
    player1_score_after = int(browser.find_element(By.CSS_SELECTOR, ".player1 .score").text)
    player2_score_after = int(browser.find_element(By.CSS_SELECTOR, ".player2 .score").text)

    # Kiểm tra kết quả
    assert player1_score_after == player1_score_initial + 1, "Player 1's score should increase by 1."
    assert player2_score_after == player2_score_initial, "Player 2's score should remain unchanged."

def test_player2_wins_player1_loses(browser):
    # Chuyển sang chế độ 2 người chơi
    mode_button = browser.find_element(By.CLASS_NAME, "swap")
    mode_button.click()

    # Lấy điểm số ban đầu của Player 1 và Player 2
    player1_score_initial = int(browser.find_element(By.CSS_SELECTOR, ".player1 .score").text)
    player2_score_initial = int(browser.find_element(By.CSS_SELECTOR, ".player2 .score").text)

    # Lấy các ô vuông trong bảng
    squares = browser.find_elements(By.CLASS_NAME, "square")

    # Player 2 thắng theo cột giữa
    moves = [0, 1, 2, 4, 3, 7]  # Player 1: 0, 2, 3; Player 2: 1, 4, 7
    for move in moves:
        squares[move].click()
        time.sleep(1)

    # Lấy điểm số sau trận đấu
    player1_score_after = int(browser.find_element(By.CSS_SELECTOR, ".player1 .score").text)
    player2_score_after = int(browser.find_element(By.CSS_SELECTOR, ".player2 .score").text)

    # Kiểm tra kết quả
    assert player2_score_after == player2_score_initial + 1, "Player 2's score should increase by 1."
    assert player1_score_after == player1_score_initial, "Player 1's score should remain unchanged."

def test_game_tie(browser):
    # Chuyển sang chế độ 2 người chơi
    mode_button = browser.find_element(By.CLASS_NAME, "swap")
    mode_button.click()

    # Lấy điểm số hòa ban đầu
    tie_score_initial = int(browser.find_element(By.CSS_SELECTOR, ".ties .score").text)

    # Lấy các ô vuông trong bảng
    squares = browser.find_elements(By.CLASS_NAME, "square")

    # Điền đầy bảng để hòa
    moves = [0, 1, 2, 4, 3, 5, 7, 6, 8]  # Tất cả các ô được điền
    for move in moves:
        squares[move].click()
        time.sleep(1)

    # Lấy điểm số hòa sau trận đấu
    tie_score_after = int(browser.find_element(By.CSS_SELECTOR, ".ties .score").text)

    # Kiểm tra kết quả
    assert tie_score_after == tie_score_initial + 1, "Tie score should increase by 1."