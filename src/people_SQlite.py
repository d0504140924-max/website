import sqlite3
from website.src.people_interface import PeopleInterface
from website.src.person import Person

class People(PeopleInterface):

    _db_path: str

    def __init__(self, db_path, person: Person):
        self._db_path = db_path
        self.person = person

    @property
    def db_path(self):
        return self._db_path
    @db_path.setter
    def db_path(self, new_path):
        assert isinstance(new_path, str)
        self._db_path = new_path

    def create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
            CREATE TABLE IF NOT EXISTS people (
            id TEXT PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            age INTEGER NOT NULL,
            phone_number TEXT,
            email TEXT)
            """)
            conn.commit()

    def add_user(self, person: Person):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
            INSERT OR IGNORE INTO people (id, first_name, last_name, age, phone_number, email)
             VALUES (?,?,?,?,?,?)""", (person.id, person.first_name, person.last_name, person.age,
                                      person.phone_number, person.email))
            conn.commit()
    def add_employee(self, person: Person):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
            INSERT OR IGNORE INTO people (id, first_name, last_name, age, phone_number, email)
             VALUES (?,?,?,?,?,?)""", (person.id, person.first_name, person.last_name, person.age,
                                          person.phone_number, person.email))
            conn.commit()

    def add_manager(self, person: Person):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
            INSERT OR IGNORE INTO people (id, first_name, last_name, age, phone_number, email)
             VALUES (?,?,?,?,?,?)""", (person.id, person.first_name, person.last_name, person.age,
                                         person.phone_number, person.email))
            conn.commit()

    def remove_person(self, person_id: str):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
            DELETE FROM people WHERE id = ?""", (person_id,))
            conn.commit()

    def get_person(self, person_id: str):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
            SELECT * FROM people WHERE id = ?""", (person_id,))
            row = cur.fetchone()
            return row

    def list_people(self):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
            SELECT * FROM people""")
            rows = cur.fetchall()
            return rows

