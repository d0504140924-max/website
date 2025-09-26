from website.src.money_interface import MoneyManagerAbc
import sqlite3
from datetime import datetime


class MoneyManage(MoneyManagerAbc):


    def __init__(self, db_path):

        self.db_path = db_path
        self.time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
            conn.commit()

    def deposit(self, amount: float):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            self.time  = getattr(self, "time", None) or datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            cur.execute("""
            INSERT INTO ledger (type, date, amount, current_amount)
                             VALUES (?, ?, ?, ?)""",('deposit',self.time, amount, self.current_amount()))
            conn.commit()

    def purchase(self, amount: float):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            self.time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            cur.execute("""
                         INSERT INTO ledger (type, date, amount, current_amount)
                         VALUES (?, ?, ?,?)""", ('purchase', self.time, amount, self.current_amount()))
            conn.commit()

    def sale(self, amount: float):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            self.time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            cur.execute("""
                         INSERT INTO ledger (type, date, amount , current_amount)
                         VALUES (?, ?, ?,?)""", ('sale',self.time, amount, self.current_amount()))
            conn.commit()

    def withdraw(self, amount: float):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            self.time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            cur.execute("""
            INSERT INTO ledger (type, date, amount, currtnt_amount) VALUES (?, ?, ?,?)""",
                         ('withdraw',self.time, amount, self.current_amount()))
            conn.commit()

    def current_amount(self):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
        SELECT
            COALESCE(SUM(CASE WHEN type IN ('deposit', 'sale') THEN amount END), 0) AS inflow,
            COALESCE(SUM(CASE WHEN type IN ('purchase', 'withdraw') THEN amount END), 0) AS outflow
        FROM ledger""")
            inflow, outflow = cur.fetchone()
            inflow = float(inflow or 0.0)
            outflow = float(outflow or 0.0)
            current_amount = inflow - outflow
            return current_amount

    def movements_record(self, type: str, start=None, end=None):
        if start is None:
            start = '01-01-0001 00:00:00'
        if end is None:
            end = '31-12-9999 23:59:59'
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
        start = start_db.strftime('%d-%m-%Y %H:%M:%S')
        end = end_db.strftime('%d-%m-%Y %H:%M:%S')
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
            SELECT 
            COALESCE(SUM(CASE WHEN type IN ('deposit', 'sale') THEN amount END), 0) AS inflow,
            COALESCE(SUM(CASE WHEN type IN ('purchase', 'withdraw') THEN amount END), 0) AS outflow
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
