import platform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_validation():
    # Выбираем браузер в зависимости от ОС
    if platform.system() == "Windows":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Safari()

    wait = WebDriverWait(driver, 10)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    # Заполняем форму
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "email").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    # Zip code оставляем пустым, как в ТЗ
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Нажимаем Submit
    driver.find_element(
        By.XPATH, "//button[text()='Submit']"
    ).click()

    # Ждём применения стилей валидации
    zip_field = wait.until(
        EC.presence_of_element_located((By.NAME, "zip"))
    )

    # Проверяем, что Zip code подсвечен красным
    assert "is-invalid" in zip_field.get_attribute("class"), (
        "Поле Zip code не подсвечено красным"
    )

    # Проверяем, что остальные поля подсвечены зеленым
    fields_to_check = [
        "first-name", "last-name", "address",
        "email", "phone", "city", "country",
        "job-position", "company"
    ]
    for field_name in fields_to_check:
        field = driver.find_element(By.NAME, field_name)
        assert "is-valid" in field.get_attribute("class"), (
            f"Поле {field_name} не подсвечено зеленым"
        )

    driver.quit()
