from website.src.money_interface import MoneyManagerAbc
import sqlite3
from datetime import datetime


class MoneyManage(MoneyManagerAbc):


    def __init__(self, db_path):
        self.db_path = db_path


    @property
    def db_path(self):
        return self._db_path
    @db_path.setter
    def db_path(self, new_db_path):
        assert isinstance(new_db_path, str)
        self._db_path = new_db_path

    def create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute('''CREATE TABLE IF NOT EXISTS ledger (
            type TEXT NOT NULL,
            date TEXT NOT NULL,
            amount REAL NOT NULL,
            current_amount REAL NOT NULL
            )''')
            cur.execute("CREATE INDEX IF NOT EXISTS idx_ledger_date ON ledger(date)")
            conn.commit()

    def deposit(self, amount: float):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            row = self.current_amount()
            if row is None:
                cur.execute("""
                            INSERT INTO ledger (type, date, amount, current_amount)
                            VALUES (?, ?, ?, ?)""", ('deposit', time, amount, amount))
            else:
                cur.execute("""
            INSERT INTO ledger (type, date, amount, current_amount)
                             VALUES (?, ?, ?, ?)""",('deposit', time, amount, row[0] + amount))
            conn.commit()


    def withdraw(self, amount: float):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            row = self.current_amount()
            if row is None:
                cur.execute("""
                            INSERT INTO ledger (type, date, amount, current_amount)
                            VALUES (?, ?, ?, ?)""",
                            ('withdraw', time, amount, -amount))
            else:
                cur.execute("""
                    INSERT INTO ledger (type, date, amount, current_amount) VALUES (?, ?, ?,?)""",
                         ('withdraw', time, amount, row[0] - amount))
            conn.commit()

    def current_amount(self):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("SELECT current_amount FROM ledger ORDER BY date DESC LIMIT 1")
            row = cur.fetchone()
            if row is None:
                return 0
            return row[0]


    def movements_record(self, type: str, start=None, end=None):
        if start is None:
            start = '0001-01-01 00:00:00'
        if end is None:
            end = '9999-12-31 23:59:59'
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
            SELECT * FROM ledger WHERE type = ? AND date BETWEEN ? AND ?""",
                         (type, start, end))
            rows = cur.fetchall()
            return rows

    def month_report(self, month: int, year: int | None = None):
        if year is None:
            year = datetime.now().year
        start_db = datetime(year,month,1, 0, 0, 0)
        if month == 12:
            end_db = datetime(year + 1,1,1,0 ,0 ,0)
        else:
            end_db = datetime(year,month + 1,1, 0, 0, 0)
        start = start_db.strftime('%Y-%m-%d %H:%M:%S')
        end = end_db.strftime('%Y-%m-%d %H:%M:%S')
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
            SELECT 
            COALESCE(SUM(CASE WHEN type IN ('deposit') THEN amount END), 0) AS inflow,
            COALESCE(SUM(CASE WHEN type IN ('withdraw') THEN amount END), 0) AS outflow
            FROM ledger WHERE date >= ? AND date < ?""",(start, end))
            inflow, outflow = cur.fetchone()
            neto = inflow - outflow
            month_report = {
            'in month': month,
            'in year': year,
            'the inflow is': inflow,
            'the outflow is': outflow,
            'neto': neto}
            return month_report
