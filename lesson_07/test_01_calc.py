from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.wait = WebDriverWait(driver, 50)  # 45 сек + запас

        # Локаторы
        self.delay_input = (By.ID, "delay")
        self.btn_7 = (By.XPATH, "//span[text()='7']")
        self.btn_plus = (By.XPATH, "//span[text()='+']")
        self.btn_8 = (By.XPATH, "//span[text()='8']")
        self.btn_eq = (By.XPATH, "//span[text()='=']")
        self.screen = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, value):
        element = self.driver.find_element(*self.delay_input)
        element.clear()
        element.send_keys(str(value))

    def click_7(self):
        self.driver.find_element(*self.btn_7).click()

    def click_plus(self):
        self.driver.find_element(*self.btn_plus).click()

    def click_8(self):
        self.driver.find_element(*self.btn_8).click()

    def click_eq(self):
        self.driver.find_element(*self.btn_eq).click()

    def get_result(self):
        result_element = self.wait.until(
            EC.visibility_of_element_located(self.screen)
        )
        return result_element.text


def test_calculator():
    driver = webdriver.Chrome()

    # 1. Создаем объект страницы
    calc_page = CalculatorPage(driver)

    # 2. Выполняем сценарий через методы страницы
    calc_page.open()
    calc_page.set_delay(45)
    calc_page.click_7()
    calc_page.click_plus()
    calc_page.click_8()
    calc_page.click_eq()

    # 3. Проверяем результат (assert только в тесте!)
    assert calc_page.get_result() == "15", (
        f"Ожидался результат '15', "
        f"получено: '{calc_page.get_result()}'"
    )

    driver.quit()
