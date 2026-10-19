import os
import requests

BASE_URL = "https://ru.yougile.com/api-v2"

YOUGILE_LOGIN = os.getenv("YOUGILE_LOGIN")
YOUGILE_PASSWORD = os.getenv("YOUGILE_PASSWORD")
YOUGILE_COMPANY_ID = os.getenv("YOUGILE_COMPANY_ID")
YOUGILE_TOKEN = os.getenv("YOUGILE_TOKEN")

if (
    not YOUGILE_TOKEN
    and YOUGILE_LOGIN
    and YOUGILE_PASSWORD
    and YOUGILE_COMPANY_ID
):
    response = requests.post(
        f"{BASE_URL}/auth/keys",
        json={
            "login": YOUGILE_LOGIN,
            "password": YOUGILE_PASSWORD,
            "companyId": YOUGILE_COMPANY_ID
        },
        headers={"Content-Type": "application/json"},
        proxies={}
    )
    if response.status_code == 201:
        YOUGILE_TOKEN = response.json()["key"]

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {YOUGILE_TOKEN}"
}
