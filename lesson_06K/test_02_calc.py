from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    driver = webdriver.Chrome()
    # Увеличиваем время ожидания (45 сек задержка + запас)
    wait = WebDriverWait(driver, 50)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "slow-calculator.html"
    )

    # Вводим задержку 45 секунд
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажимаем кнопки калькулятора
    driver.find_element(
        By.XPATH, "//span[text()='7']"
    ).click()
    driver.find_element(
        By.XPATH, "//span[text()='+']"
    ).click()
    driver.find_element(
        By.XPATH, "//span[text()='8']"
    ).click()
    driver.find_element(
        By.XPATH, "//span[text()='=']"
    ).click()

    # Ждём появления результата 15 на экране
    result_screen = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "screen")
        )
    )

    assert result_screen.text == "15", (
        f"Ожидался результат '15', "
        f"но получено: '{result_screen.text}'"
    )

    driver.quit()
