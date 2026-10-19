def _get_token(self):
    """Получает токен через API."""
    login = os.getenv("YOUGILE_LOGIN")
    password = os.getenv("YOUGILE_PASSWORD")
    company_id = os.getenv("YOUGILE_COMPANY_ID")

    if not login or not password or not company_id:
        raise Exception(
            "Не установлены переменные окружения: "
            "YOUGILE_LOGIN, YOUGILE_PASSWORD, YOUGILE_COMPANY_ID"
        )

    response = requests.post(
        f"{self.base_url}/auth/keys",
        json={
            "login": login,
            "password": password,
            "companyId": company_id
        },
        headers={"Content-Type": "application/json"},
        proxies=self.proxies
    )

    if response.status_code == 201:
        return response.json()["key"]
    raise Exception(
        f"Не удалось получить токен: {response.status_code}"
    )
