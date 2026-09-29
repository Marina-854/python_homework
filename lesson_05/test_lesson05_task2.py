from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    # Находим поле ввода по name="custname"
    input_field = driver.find_element(By.NAME, "custname")

    # Вводим имя
    input_field.send_keys("Марина")

    # Находим кнопку и кликаем
    xpath = "//button[contains(text(), 'Отправить')]"
    button = driver.find_element(By.XPATH, xpath)
    button.click()

    # Проверяем что URL изменился после отправки формы
    assert (
        "submitted" in driver.current_url
        or "Form" in driver.current_url
        or driver.current_url
        != "https://httpbin.qa-territory.online/forms/post"
    )

    driver.quit()
