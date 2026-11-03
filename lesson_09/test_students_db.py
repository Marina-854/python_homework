import uuid
from db_client import StudentTable, CONNECTION_STRING

db = StudentTable(CONNECTION_STRING)


def test_add_student():
    """Тест на добавление нового студента в БД"""
    unique_id = 100000 + int(uuid.uuid4().hex[:6], 16)
    db.create_student(unique_id, "beginner", "full-time", 1)
    students = db.get_student_by_id(unique_id)
    assert len(students) == 1
    assert students[0]["user_id"] == unique_id
    db.delete_student(unique_id)


def test_update_student():
    """Тест на изменение данных существующего студента"""
    unique_id = 200000 + int(uuid.uuid4().hex[:6], 16)
    db.create_student(unique_id, "beginner", "full-time", 1)
    db.update_student_level(unique_id, "advanced")
    students = db.get_student_by_id(unique_id)
    assert len(students) == 1
    assert students[0]["level"] == "advanced"
    db.delete_student(unique_id)


def test_delete_student():
    """Тест на удаление студента из БД"""
    unique_id = 300000 + int(uuid.uuid4().hex[:6], 16)
    db.create_student(unique_id, "beginner", "part-time", 2)
    db.delete_student(unique_id)
    students = db.get_student_by_id(unique_id)
    assert len(students) == 0
