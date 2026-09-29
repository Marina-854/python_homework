from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    # Открываем главную страницу
    driver.get("https://httpbin.qa-territory.online")

    # Находим и кликаем на ссылку "HTML Form"
    link = driver.find_element(By.LINK_TEXT, "HTML Form")
    link.click()

    # Проверяем что URL изменился на /forms/post
    assert "/forms/post" in driver.current_url

    # Возвращаемся назад
    driver.back()

    # Проверяем что вернулись на главную
    assert "httpbin.qa-territory.online" in driver.current_url

    driver.quit()
