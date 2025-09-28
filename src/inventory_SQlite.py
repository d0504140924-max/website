from website.src.inventory_interface import InventoryManage
from website.src.product import Product
from pathlib import Path
import sqlite3



class TheInventory(InventoryManage):


    _db_path: str


    def __init__(self, db_path):
        self.db_path = db_path



    def create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS products(
                    id TEXT PRIMARY KEY NOT NULL,
                    category TEXT NOT NULL,
                    name TEXT NOT NULL,
                    manufacturer TEXT NOT NULL,
                    price REAL NOT NULL,
                    cost REAL NOT NULL
                )""")

            cur.execute("""
                CREATE TABLE IF NOT EXISTS inventory(
                    product_id TEXT PRIMARY KEY NOT NULL, 
                    amount INTEGER NOT NULL DEFAULT 0
                )""")
            conn.commit()


    @property
    def db_path(self):
        return self._db_path
    @db_path.setter
    def db_path(self, new_path1):
        assert isinstance(new_path1, str)
        self._db_path = new_path1



    def get_item_amount(self, id_item: str):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
            SELECT amount FROM inventory WHERE product_id = ?""", (id_item,))
            row = cur.fetchone()
            return row[0] if row else None


    def add_item(self, item: Product, num=1):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
            INSERT OR IGNORE INTO products (id, category, name, manufacturer,
                     price, cost) VALUES (?, ?, ?, ?, ?, ?)""",
                    (item.id, item.category, item.name,
                     item.manufacturer, item.price, item.cost))
            cur.execute("""
            INSERT OR IGNORE INTO inventory (product_id, amount) VALUES (?, ?)""",
                    (item.id, num))
            conn.commit()

    def remove_item(self, item_id: str):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
            DELETE FROM products WHERE id=?""",
                    (item_id,))
            cur.execute("""
                    DELETE FROM inventory WHERE product_id = ?""",
                    (item_id,))
            conn.commit()



    def update_amount(self, item_id: str, new_amount: int):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""SELECT 1 FROM inventory WHERE product_id = ?""",(item_id,))
            row = cur.fetchone()
            if row is None:
                raise Exception('Item not found')
            if new_amount == 0:
                raise ValueError('new_amount must be positive or negative')
            cur.execute("""
                UPDATE inventory SET amount = amount + ? WHERE product_id = ?""",
                (new_amount, item_id))
            conn.commit()


    def show_inventory(self):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""SELECT * FROM inventory""")
            rows = cur.fetchall()
            return rows

    def show_one_category(self, category: str):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""SELECT 1 FROM products WHERE category = ?""", (category,))
            _row = cur.fetchone()
            if _row is None:
                raise Exception('Category not found')
            cur.execute("""
            SELECT name, price FROM products WHERE category = ?""",(category,))
            rows = cur.fetchall()
            return rows

    def get_item_by_id(self, item_id: str):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
            SELECT * FROM products WHERE id = ?""",(item_id,))
            _row = cur.fetchone()
            return _row




