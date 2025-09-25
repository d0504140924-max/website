from website.src.InventoryManage_interface import InventoryManage
from website.src.product import Product
import sqlite3



class TheInventory(InventoryManage):


    _db_path: str


    def __init__(self, db_path):
        self.db_path = db_path
        self._conn = sqlite3.connect(self.db_path)
        self._cur = self._conn.cursor()


    def create_table(self):
        self._cur.execute("""
                CREATE TABLE IF NOT EXISTS products(
                    id TEXT PRIMARY KEY NOT NULL,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    manufacturer TEXT NOT NULL,
                    price REAL NOT NULL,
                    cost REAL NOT NULL
                )""")

        self._cur.execute("""
                CREATE TABLE IF NOT EXISTS inventory(
                    product_id TEXT PRIMARY KEY NOT NULL, 
                    amount INTEGER NOT NULL DEFAULT 0
                )""")
        self._conn.commit()

    def close(self):
        self._conn.close()

    @property
    def db_path(self):
        return self._db_path
    @db_path.setter
    def db_path(self, new_path1):
        assert isinstance(new_path1, str)
        self._db_path = new_path1



    def get_amount(self, id_item: str):
         self._cur.execute("""
         SELECT amount FROM inventory WHERE product_id = ?""", (id_item,))
         row = self._cur.fetchone()
         return row[0] if row else None


    def add_item(self, item: Product, num=1):
        self._cur.execute("""
        INSERT OR IGNORE INTO products (id, name, category, manufacturer,
                     price, cost) VALUES (?, ?, ?, ?, ?, ?)""",
                    (item.id, item.name, item.category,
                     item.manufacturer, item.price, item.cost))
        self._cur.execute("""
        INSERT OR IGNORE INTO inventory (product_id, amount) VALUES (?, ?)""",
                    (item.id, num))
        self._conn.commit()

    def remove_item(self, item: Product):
        self._cur.execute("""
        DELETE FROM products WHERE id=?""",
                    (item.id,))
        self._cur.execute("""
                    DELETE FROM inventory WHERE product_id = ?""",
                    (item.id,))
        self._conn.commit()



    def update_amount(self, item_id: str, new_amount: int):
        self._cur.execute("""SELECT 1 FROM inventory WHERE product_id = ?""",(item_id,))
        row = self._cur.fetchone()
        if row is None:
            raise Exception('Item not found')
        if new_amount == 0:
            raise ValueError('new_amount must be positive or negative')
        self._cur.execute("""
            UPDATE inventory SET amount = amount + ? WHERE product_id = ?""",
            (new_amount, item_id))
        self._conn.commit()


    def show_inventory(self):
        self._cur.execute("""SELECT * FROM inventory""")
        rows = self._cur.fetchall()
        return rows

    def show_one_category(self, category: str):
        self._cur.execute("""SELECT 1 FROM products WHERE category = ?""", (category,))
        _row = self._cur.fetchone()
        if _row is None:
            raise Exception('Category not found')
        self._cur.execute("""
        SELECT name, price FROM products WHERE category = ?""",(category,))
        rows = self._cur.fetchall()
        return rows




