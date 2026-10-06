from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # 1. Откройте страницу
    driver.get(
        "https://the-internet.herokuapp.com/dynamic_loading/2"
    )

    # 2. Найдите и нажмите на кнопку "Start"
    start_btn = driver.find_element(By.CSS_SELECTOR, "button")
    start_btn.click()

    # 3. Дождитесь появления текста "Hello World!"
    hello_element = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//h4[text()='Hello World!']")
        )
    )

    # 4. Сделайте скриншот страницы
    driver.save_screenshot("lesson_06/hello_world.png")

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    assert hello_element.text == "Hello World!", (
        f"Ожидался 'Hello World!', получено: '{hello_element.text}'"
    )

    driver.quit()
