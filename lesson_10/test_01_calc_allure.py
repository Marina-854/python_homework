import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Page Object для страницы медленного калькулятора.
    URL: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
    """

    def __init__(self, driver) -> None:
        """
        Инициализация страницы калькулятора.

        :param driver: экземпляр WebDriver
        :return: None
        """
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.wait = WebDriverWait(driver, 60)

        self.delay_input = (By.ID, "delay")
        self.btn_7 = (By.XPATH, "//span[text()='7']")
        self.btn_plus = (By.XPATH, "//span[text()='+']")
        self.btn_8 = (By.XPATH, "//span[text()='8']")
        self.btn_eq = (By.XPATH, "//span[text()='=']")
        self.screen = (By.CLASS_NAME, "screen")

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """
        Открывает страницу калькулятора в браузере.

        :return: None
        """
        self.driver.get(self.url)

    @allure.step("Установить задержку {value} секунд")
    def set_delay(self, value: int) -> None:
        """
        Устанавливает задержку для выполнения операций.

        :param value: значение задержки в секундах (int)
        :return: None
        """
        element = self.driver.find_element(*self.delay_input)
        element.clear()
        element.send_keys(str(value))

    @allure.step("Нажать кнопку '7'")
    def click_7(self) -> None:
        """
        Нажимает кнопку '7' на калькуляторе.

        :return: None
        """
        self.driver.find_element(*self.btn_7).click()

    @allure.step("Нажать кнопку '+'")
    def click_plus(self) -> None:
        """
        Нажимает кнопку '+' на калькуляторе.

        :return: None
        """
        self.driver.find_element(*self.btn_plus).click()

    @allure.step("Нажать кнопку '8'")
    def click_8(self) -> None:
        """
        Нажимает кнопку '8' на калькуляторе.

        :return: None
        """
        self.driver.find_element(*self.btn_8).click()

    @allure.step("Нажать кнопку '='")
    def click_eq(self) -> None:
        """
        Нажимает кнопку '=' на калькуляторе.

        :return: None
        """
        self.driver.find_element(*self.btn_eq).click()

    @allure.step("Получить результат с экрана калькулятора")
    def get_result(self) -> str:
        """
        Возвращает результат вычислений с экрана калькулятора.

        :return: строка с результатом (str)
        """
        # Ждём появления результата до 60 секунд
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), "15"
            )
        )
        return self.driver.find_element(
            By.CLASS_NAME, "screen"
        ).text


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculatorAllure:
    """Тесты для медленного калькулятора с интеграцией Allure."""

    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        """
        Фикстура для инициализации и завершения работы драйвера.

        :return: None
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.quit()

    @allure.title("Вычисление: 7 + 8 = 15")
    @allure.description(
        "Тест проверяет корректность сложения 7 + 8 "
        "на медленном калькуляторе с задержкой 45 секунд."
    )
    @allure.story("Арифметические операции")
    def test_calculator(self) -> None:
        """
        Тест проверяет работу калькулятора: 7 + 8 = 15.

        :return: None
        """
        calc_page = CalculatorPage(self.driver)

        with allure.step("Открыть страницу калькулятора"):
            calc_page.open()

        with allure.step("Установить задержку 45 секунд"):
            calc_page.set_delay(45)

        with allure.step("Нажать кнопки: 7, +, 8, ="):
            calc_page.click_7()
            calc_page.click_plus()
            calc_page.click_8()
            calc_page.click_eq()

        with allure.step("Проверить, что результат равен 15"):
            assert calc_page.get_result() == "15", (
                f"Ожидался результат '15', "
                f"получено: '{calc_page.get_result()}'"
            )
