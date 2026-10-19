import pytest
import uuid
from api_client import YougileAPI

api = YougileAPI()


@pytest.fixture(scope="function")
def project_id():
    """
    Фикстура для стабильности тестов.
    SETUP: Создает проект перед тестом.
    TEARDOWN: Удаляет проект после теста.
    """
    unique_title = f"TestProject_{uuid.uuid4().hex[:8]}"
    resp = api.create_project(unique_title)

    assert resp.status_code in [200, 201], (
        f"Не удалось создать проект: {resp.status_code}"
    )

    created_id = resp.json()["id"]
    yield created_id

    api.delete_project(created_id)


# ==========================================
# POST /api-v2/projects
# ==========================================

def test_create_project_positive():
    """Позитивный тест: успешное создание проекта"""
    unique_title = f"NewProject_{uuid.uuid4().hex[:8]}"
    resp = api.create_project(unique_title)

    assert resp.status_code in [200, 201], (
        f"Ожидался 200/201, получен {resp.status_code}"
    )
    assert "id" in resp.json(), "В ответе отсутствует поле id"

    api.delete_project(resp.json()["id"])


def test_create_project_negative_empty_title():
    """Негативный тест: создание проекта с пустым названием"""
    resp = api.create_project("")
    assert resp.status_code == 400, (
        f"Ожидался 400, получен {resp.status_code}"
    )


# ==========================================
# GET /api-v2/projects/{id}
# ==========================================

def test_get_project_positive(project_id):
    """Позитивный тест: успешное получение существующего проекта"""
    resp = api.get_project(project_id)

    assert resp.status_code == 200, (
        f"Ожидался 200, получен {resp.status_code}"
    )
    assert resp.json()["id"] == project_id


def test_get_project_negative_not_found():
    """Негативный тест: получение несуществующего проекта"""
    fake_id = "00000000-0000-0000-0000-000000000000"
    resp = api.get_project(fake_id)

    assert resp.status_code == 404, (
        f"Ожидался 404, получен {resp.status_code}"
    )


# ==========================================
# PUT /api-v2/projects/{id}
# ==========================================

def test_update_project_positive(project_id):
    """Позитивный тест: успешное обновление проекта"""
    new_title = f"Updated_{uuid.uuid4().hex[:8]}"
    resp = api.update_project(project_id, title=new_title)

    assert resp.status_code == 200, (
        f"Ожидался 200, получен {resp.status_code}"
    )


def test_update_project_negative_not_found():
    """Негативный тест: обновление несуществующего проекта"""
    fake_id = "00000000-0000-0000-0000-000000000000"
    resp = api.update_project(fake_id, title="Fake Title")

    assert resp.status_code == 404, (
        f"Ожидался 404, получен {resp.status_code}"
    )
