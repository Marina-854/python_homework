import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object для страницы авторизации в магазине."""

    def __init__(self, driver) -> None:
        """
        Инициализация страницы авторизации.

        :param driver: экземпляр WebDriver
        :return: None
        """
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")

    @allure.step("Открыть страницу авторизации")
    def open(self) -> None:
        """
        Открывает страницу авторизации.

        :return: None
        """
        self.driver.get(self.url)

    @allure.step(
        "Ввести логин '{username}' и пароль '{password}'"
    )
    def login(self, username: str, password: str) -> None:
        """
        Вводит учетные данные и нажимает кнопку входа.

        :param username: имя пользователя (str)
        :param password: пароль пользователя (str)
        :return: None
        """
        self.driver.find_element(
            *self.username_input
        ).send_keys(username)
        self.driver.find_element(
            *self.password_input
        ).send_keys(password)
        self.driver.find_element(*self.login_btn).click()


class MainShopPage:
    """Page Object для главной страницы магазина."""

    def __init__(self, driver) -> None:
        """
        Инициализация главной страницы магазина.

        :param driver: экземпляр WebDriver
        :return: None
        """
        self.driver = driver
        self.add_to_cart_btn = (
            By.ID, "add-to-cart-sauce-labs-backpack"
        )
        self.cart_btn = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step(
        "Добавить товар 'Sauce Labs Backpack' в корзину"
    )
    def add_backpack_to_cart(self) -> None:
        """
        Нажимает кнопку добавления товара в корзину.

        :return: None
        """
        self.driver.find_element(
            *self.add_to_cart_btn
        ).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """
        Нажимает на иконку корзины.

        :return: None
        """
        self.driver.find_element(*self.cart_btn).click()


class CartPage:
    """Page Object для страницы корзины."""

    def __init__(self, driver) -> None:
        """
        Инициализация страницы корзины.

        :param driver: экземпляр WebDriver
        :return: None
        """
        self.driver = driver
        self.checkout_btn = (By.ID, "checkout")
        self.item_name = (By.CLASS_NAME, "inventory_item_name")

    @allure.step("Нажать кнопку 'Checkout'")
    def click_checkout(self) -> None:
        """
        Переходит к оформлению заказа.

        :return: None
        """
        self.driver.find_element(*self.checkout_btn).click()

    @allure.step("Получить название товара в корзине")
    def get_item_name(self) -> str:
        """
        Возвращает название товара в корзине.

        :return: название товара (str)
        """
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            EC.visibility_of_element_located(self.item_name)
        )
        return element.text


class CheckoutPage:
    """Page Object для страницы оформления заказа."""

    def __init__(self, driver) -> None:
        """
        Инициализация страницы оформления заказа.

        :param driver: экземпляр WebDriver
        :return: None
        """
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")
        self.finish_btn = (By.ID, "finish")
        self.success_message = (
            By.CLASS_NAME, "complete-header"
        )

    @allure.step(
        "Заполнить данные: Имя '{first}', "
        "Фамилия '{last}', Индекс '{postal}'"
    )
    def fill_checkout_info(
        self, first: str, last: str, postal: str
    ) -> None:
        """
        Заполняет форму контактных данных.

        :param first: имя (str)
        :param last: фамилия (str)
        :param postal: почтовый индекс (str)
        :return: None
        """
        self.driver.find_element(
            *self.first_name_input
        ).send_keys(first)
        self.driver.find_element(
            *self.last_name_input
        ).send_keys(last)
        self.driver.find_element(
            *self.postal_code_input
        ).send_keys(postal)
        self.driver.find_element(
            *self.continue_btn
        ).click()

    @allure.step("Завершить заказ")
    def finish_order(self) -> None:
        """
        Нажимает кнопку завершения заказа.

        :return: None
        """
        self.driver.find_element(*self.finish_btn).click()

    @allure.step(
        "Получить текст сообщения об успешном завершении"
    )
    def get_success_message(self) -> str:
        """
        Возвращает текст сообщения об успехе.

        :return: текст сообщения (str)
        """
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
            EC.visibility_of_element_located(
                self.success_message
            )
        )
        return element.text


@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
class TestShopAllure:
    """Тесты для интернет-магазина с Allure."""

    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        """
        Фикстура для инициализации драйвера.

        :return: None
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.quit()

    @allure.title("Полный цикл покупки товара в магазине")
    @allure.description(
        "Тест проверяет сценарий: авторизация, добавление "
        "товара в корзину, оформление заказа и проверка "
        "успешного завершения."
    )
    @allure.story("Покупка товара")
    def test_shop_flow(self) -> None:
        """
        Тест полного цикла покупки.

        :return: None
        """
        login_page = LoginPage(self.driver)
        main_page = MainShopPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)

        with allure.step("Авторизация в системе"):
            login_page.open()
            login_page.login(
                "standard_user", "secret_sauce"
            )

        with allure.step("Добавление товара в корзину"):
            main_page.add_backpack_to_cart()
            main_page.go_to_cart()

        with allure.step(
            "Проверка наличия товара в корзине"
        ):
            item_name = cart_page.get_item_name()
            assert item_name == "Sauce Labs Backpack", (
                f"Товар не найден в корзине, получено: {item_name}"
            )
            cart_page.click_checkout()

        with allure.step("Оформление заказа"):
            checkout_page.fill_checkout_info(
                "Ivan", "Ivanov", "123456"
            )
            checkout_page.finish_order()

        with allure.step(
            "Проверка успешного завершения заказа"
        ):
            success_msg = checkout_page.get_success_message()
            assert (
                "Thank you for your order!" in success_msg
            ), f"Сообщение об успехе не отображается, получено: {success_msg}"
