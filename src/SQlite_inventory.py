from website.src.InventoryManage_interface import InventoryManage
from website.src.product import Product
from website.src.create_db import create_db
import sqlite3



class TheInventory(InventoryManage):


    _db_path: str


    def __init__(self, db_path):
        self.db_path = db_path


    @property
    def db_path(self):
        return create_db(self.db_path)
    @db_path.setter
    def db_path(self, new_path1):
        assert isinstance(new_path1, str)
        self._db_path = new_path1



    @property
    def table(self):
        return sqlite3.connect(self.db_path)

    @property
    def cur(self):
        cur = self.table.cursor()
        return cur



    def get_amount(self, id_item):
         self.cur.execute("""
         SELECT amount FROM inventory WHERE product_id = ?""", (id_item,))
         row = self.cur.fetchall()
         return row


    def add_item(self, item: Product, num=1):
        self.cur.execute(""""
        INSERT OR IGNOR INTO products (id, name, category, manufacturer,
                     price, cost) VALUES (?, ?, ?, ?, ?, ?)""",
                    (item.id, item.name, item.category,
                     item.manufacturer, item.price, item.cost))
        self.cur.execute("""
        INSERT OR IGNOR INTO inventory (product_id, amount) VALUES (?, ?)""",
                    (item.id, num))
        self.table.commit()

    def remove_item(self, item: Product):
        self.cur.execute("""
        DELETE FROM products WHERE id=?,""",
                    (item.id,))
        self.cur.execute("""
                    DELETE FROM inventory WHERE product_id = ?""",
                    (item.id,))
        self.table.commit()



    def update_amount(self, item_id: str, new_amount: int):
        self.cur.execute("""SELECT 1 FROM inventory WHERE product_id = ?""",(item_id,))
        row = self.cur.fetchone()
        if row is None:
            raise Exception('Item not found')
        if new_amount == 0:
            raise ValueError('new_amount must be positive or negative')
        self.cur.execute("""
            UPDATE inventory SET amount = amount - ? WHERE product_id = ?""",
            (new_amount, item_id))
        self.table.commit()


    def show_inventory(self):
        self.cur.execute("""SELECT * FROM inventory""")
        rows = self.cur.fetchall()
        return rows

    def show_one_category(self, category):
        self.cur.execute("""SELECT 1 FROM product WHERE category = ?""", (category,))
        _row = self.cur.fetchone()
        if _row is None:
            raise Exception('Category not found')
        self.cur.execute("""
        SELECT name, price FROM products WHERE category = ?""",(category,))
        rows = self.cur.fetchall()
        return rows




