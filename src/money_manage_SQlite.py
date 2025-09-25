from website.src.money_interface import MoneyManagerAbc
import sqlite3
from datetime import datetime

class MoneyManage(MoneyManagerAbc):


    def __init__(self, db_path):

        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()
        self.time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @property
    def db_path(self):
        return self._db_path
    @db_path.setter
    def db_path(self, new_db_path):
        assert isinstance(new_db_path, str)
        self._db_path = new_db_path

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS ledger (
        type TEXT NOT NULL,
        date TEXT NOT NULL,
        amount REAL NOT NULL
        )''')
        self.conn.commit()

    def close(self):
        self.conn.close()

    def deposit(self, amount: float):
        self.time  = getattr(self, "time", None) or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cur.execute("""
        INSERT INTO ledger (type, date, amount)
                         VALUES (?, ?, ?)""",('deposit',self.time, amount))
        self.conn.commit()

    def purchase(self, amount: float):
        self.time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cur.execute("""
                         INSERT INTO ledger (type, date, amount)
                         VALUES (?, ?, ?)""", ('purchase', self.time, amount))
        self.conn.commit()

    def sale(self, amount: float):
        self.time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cur.execute("""
                         INSERT INTO ledger (type, date, amount)
                         VALUES (?, ?, ?)""", ('sale',self.time, amount))
        self.conn.commit()

    def withdraw(self, amount: float):
        self.time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cur.execute("""
        INSERT INTO ledger (type, date, amount) VALUES (?, ?, ?)""",
                         ('withdraw',self.time, amount))
        self.conn.commit()

    def current_amount(self):
        self.cur.execute("""
        SELECT
            COALESCE(SUM(CASE WHEN type IN ('deposit', 'sale') THEN amount END), 0) AS inflow,
            COALESCE(SUM(CASE WHEN type IN ('purchase', 'withdraw') THEN amount END), 0) AS outflow
        FROM ledger""")
        inflow, outflow = self.cur.fetchone()
        inflow = float(inflow or 0.0)
        outflow = float(outflow or 0.0)
        current_amount = inflow - outflow
        return current_amount

    def movements_record(self, type: str, start=None, end=None):
        if start is None:
            start = '0001-01-01 00:00:00'
        if end is None:
            end = '9999-12-31 23:59:59'
        self.cur.execute("""
        SELECT * FROM ledger WHERE type = ? AND date BETWEEN ? AND ?""",
                         (type, start, end))
        rows = self.cur.fetchall()
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
        self.cur.execute("""
        SELECT 
            COALESCE(SUM(CASE WHEN type IN ('deposit', 'sale') THEN amount END), 0) AS inflow,
            COALESCE(SUM(CASE WHEN type IN ('purchase', 'withdraw') THEN amount END), 0) AS outflow
        FROM ledger WHERE date >= ? AND date < ?""",(start, end))
        inflow, outflow = self.cur.fetchone()
        neto = inflow - outflow
        month_report = {
            'in month': month,
            'in year': year,
            'the inflow is': inflow,
            'the outflow is': outflow,
            'neto': neto}
        return month_report
