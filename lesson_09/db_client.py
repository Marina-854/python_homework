import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")

CONNECTION_STRING = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


class StudentTable:
    """Класс для работы с таблицей student (Паттерн Page Object)"""

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)
        self.__scripts = {
            "insert": text(
                "INSERT INTO student "
                "(user_id, level, education_form, subject_id) "
                "VALUES (:user_id, :level, :education_form, :subject_id)"
            ),
            "select_by_id": text(
                "SELECT user_id, level, education_form, subject_id "
                "FROM student "
                "WHERE user_id = :student_id"
            ),
            "update": text(
                "UPDATE student "
                "SET level = :new_level "
                "WHERE user_id = :student_id"
            ),
            "delete": text(
                "DELETE FROM student WHERE user_id = :student_id"
            ),
        }

    def create_student(self, user_id, level, education_form, subject_id):
        """Добавляет нового студента"""
        conn = self.__db.connect()
        try:
            conn.execute(
                self.__scripts["insert"],
                {
                    "user_id": user_id,
                    "level": level,
                    "education_form": education_form,
                    "subject_id": subject_id,
                },
            )
            conn.commit()
        finally:
            conn.close()

    def get_student_by_id(self, student_id):
        """Получает студента по ID"""
        conn = self.__db.connect()
        try:
            result = conn.execute(
                self.__scripts["select_by_id"],
                {"student_id": student_id},
            )
            return result.mappings().all()
        finally:
            conn.close()

    def update_student_level(self, student_id, new_level):
        """Обновляет уровень студента"""
        conn = self.__db.connect()
        try:
            conn.execute(
                self.__scripts["update"],
                {"new_level": new_level, "student_id": student_id},
            )
            conn.commit()
        finally:
            conn.close()

    def delete_student(self, student_id):
        """Удаляет студента"""
        conn = self.__db.connect()
        try:
            conn.execute(
                self.__scripts["delete"],
                {"student_id": student_id},
            )
            conn.commit()
        finally:
            conn.close()
