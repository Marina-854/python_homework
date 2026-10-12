from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_sauce_demo_purchase():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Добавляем товары в корзину
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # Переходим в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Нажимаем Checkout
    driver.find_element(By.ID, "checkout").click()

    # Заполняем форму ВАШИМИ данными
    driver.find_element(By.ID, "first-name").send_keys("Марина")
    driver.find_element(By.ID, "last-name").send_keys("Трояновская")
    driver.find_element(By.ID, "postal-code").send_keys("606170")

    # Нажимаем Continue
    driver.find_element(By.ID, "continue").click()

    # Читаем итоговую стоимость
    total_element = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label")
        )
    )
    total_text = total_element.text

    # Проверяем сумму (ПРОВЕРКА ДО ЗАКРЫТИЯ БРАУЗЕРА)
    assert "$58.29" in total_text, (
        f"Ожидалась сумма $58.29, "
        f"но получено: '{total_text}'"
    )

    # Закрываем браузер
    driver.quit()
