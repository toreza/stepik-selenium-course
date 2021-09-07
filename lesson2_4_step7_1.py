from selenium.webdriver.common.by import By
# импорт из библиотеке selenium методов и полей класса By
from selenium.webdriver.support.ui import WebDriverWait
# импорт из библиотеке selenium WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# импорт из библиотеке selenium expected_conditions
from selenium import webdriver
# импорт из библиотеке selenium webdriver
import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait2.html")
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text
# слово есть в тексте сообщения
finally:
    time.sleep(10)
    browser.quit()  # выход из браузера
