import sqlite3
from datetime import datetime
from models.user import UserToCreate, UserInDb
from database import get_connection, init_db

init_db()


def _row_to_user(row: sqlite3.Row) -> UserInDb:
    return UserInDb(
        id=row["id"],
        name=row["name"],
        email=row["email"],
        phone=row["phone"],
        password=row["password"],
    )


class UserRepository:
    def get_user_by_id(self, user_id: int) -> UserInDb | None:
        with get_connection() as connection:
            row = connection.execute(
                "SELECT * FROM users WHERE id = ?", (user_id,)
            ).fetchone()
        return _row_to_user(row) if row else None

    def get_user_by_email(self, email: str) -> UserInDb | None:
        with get_connection() as connection:
            row = connection.execute(
                "SELECT * FROM users WHERE email = ?", (email,)
            ).fetchone()
        return _row_to_user(row) if row else None

    def get_user_by_phone(self, phone: str) -> UserInDb | None:
        with get_connection() as connection:
            row = connection.execute(
                "SELECT * FROM users WHERE phone = ?", (phone,)
            ).fetchone()
        return _row_to_user(row) if row else None

    def create_user(self, user_data: UserToCreate) -> UserInDb:
        now = datetime.now().isoformat()
        with get_connection() as connection:
            cursor = connection.execute(
                """
                INSERT INTO users (name, email, phone, password, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (user_data.name, user_data.email, user_data.phone,
                user_data.password, now, now),
            )
            user_id = cursor.lastrowid
        return self.get_user_by_id(user_id)

    def update_user(self, user_id: int, user_data: UserToCreate) -> UserInDb:
        now = datetime.now().isoformat()
        with get_connection() as connection:
            connection.execute(
                """
                UPDATE users
                SET name = ?, email = ?, phone = ?, password = ?, updated_at = ?
                WHERE id = ?
                """,
                (user_data.name, user_data.email, user_data.phone,
                user_data.password, now, user_id),
            )
        return self.get_user_by_id(user_id)

    def delete_user(self, user_id: int) -> None:
        with get_connection() as connection:
            connection.execute("DELETE FROM users WHERE id = ?", (user_id,))
