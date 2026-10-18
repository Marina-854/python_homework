from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(
            *self.username_input
        ).send_keys(username)
        self.driver.find_element(
            *self.password_input
        ).send_keys(password)
        self.driver.find_element(*self.login_btn).click()


class MainShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.backpack_btn = (
            By.ID, "add-to-cart-sauce-labs-backpack"
        )
        self.tshirt_btn = (
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        )
        self.onesie_btn = (
            By.ID, "add-to-cart-sauce-labs-onesie"
        )
        self.cart_link = (
            By.CLASS_NAME, "shopping_cart_link"
        )

    def add_backpack(self):
        self.driver.find_element(*self.backpack_btn).click()

    def add_tshirt(self):
        self.driver.find_element(*self.tshirt_btn).click()

    def add_onesie(self):
        self.driver.find_element(*self.onesie_btn).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_btn = (By.ID, "checkout")

    def click_checkout(self):
        self.driver.find_element(*self.checkout_btn).click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_info(self, first_name, last_name, postal_code):
        self.driver.find_element(
            *self.first_name_input
        ).send_keys(first_name)
        self.driver.find_element(
            *self.last_name_input
        ).send_keys(last_name)
        self.driver.find_element(
            *self.postal_code_input
        ).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(*self.continue_btn).click()

    def get_total(self):
        total_element = self.wait.until(
            EC.visibility_of_element_located(self.total_label)
        )
        return total_element.text


def test_shop_purchase():
    driver = webdriver.Firefox()

    # 1. Авторизация
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # 2. Добавление товаров
    inventory_page = MainShopPage(driver)
    inventory_page.add_backpack()
    inventory_page.add_tshirt()
    inventory_page.add_onesie()
    inventory_page.go_to_cart()

    # 3. Переход к оформлению
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # 4. Заполнение данных и проверка (ВАШИ ДАННЫЕ)
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_info("Марина", "Трояновская", "606170")
    checkout_page.click_continue()

    total = checkout_page.get_total()

    # 5. Проверка (assert только в тесте!)
    assert "$58.29" in total, (
        f"Ожидалась сумма $58.29, получено: '{total}'"
    )

    # 6. Закрытие браузера
    driver.quit()
