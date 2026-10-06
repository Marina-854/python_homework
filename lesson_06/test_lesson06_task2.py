from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    # Cookie пользователя 1 (Марина Трояновская)
    user1_cookie = {
        "name": "domain_sid",
        "value": "k9-z-Ayh9de3x7iGBetvP%3A1791304617466",
        "domain": "gitflic.ru"
    }

    # Cookie пользователя 2 (Марина Крутова)
    user2_cookie = {
        "name": "domain_sid",
        "value": "8MwlelcBg9KiTIfpHUKFE%3A1791303464569",
        "domain": "gitflic.ru"
    }

    # === ПОЛЬЗОВАТЕЛЬ 1 ===
    driver.get("https://gitflic.ru/")
    driver.add_cookie(user1_cookie)
    driver.refresh()

    # Перейдите на страницу пользователя 1
    profile_link = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href*='/user/']")
        )
    )
    profile_link.click()

    # Сохраните текущий URL
    user1_url = driver.current_url
    print(f"URL пользователя 1: {user1_url}")

    # Разлогиньтесь (очистите куки)
    driver.delete_all_cookies()
    driver.refresh()

    # === ПОЛЬЗОВАТЕЛЬ 2 ===
    driver.get("https://gitflic.ru/")
    driver.add_cookie(user2_cookie)
    driver.refresh()

    # Перейдите на страницу пользователя 2
    profile_link_2 = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href*='/user/']")
        )
    )
    profile_link_2.click()

    # Сохраните текущий URL
    user2_url = driver.current_url
    print(f"URL пользователя 2: {user2_url}")

    # Проверьте, что URL различаются
    assert user1_url != user2_url, (
        f"URL профилей совпадают: {user1_url} == {user2_url}"
    )

    driver.quit()
