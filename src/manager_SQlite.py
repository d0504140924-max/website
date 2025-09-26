import sqlite3
from website.src.inventory_SQlite import TheInventory
from website.src.manager_interface import ManagerAbc
from website.src.money_SQlite import MoneyManage
from website.src.person import Person
from website.src.product import Product

class Manager(ManagerAbc, Person):

    def __init__(self, db_path):
        super().__init__(Person.id, Person.first_name, Person.last_name, Person.age,
                        Person.birthday, Person.phone_number, Person.email)
        self.db_path = db_path
        self.inv = TheInventory(self.db_path)
        self.money = MoneyManage(self.db_path)

    @property
    def db_path(self):
        return self._db_path
    @db_path.setter
    def db_path(self, new_db_path):
        assert isinstance(new_db_path, str)
        self._db_path = new_db_path

    def purchase_item(self, item: Product, num: int=1):
        self.inv.add_item(item, num)
        self.inv.update_amount(item.id, num)
        self.money.purchase(item.cost)

    def change_price(self, item_id: str, new_price):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("UPDATE products SET price = ? WHERE id =?",(new_price, item_id))
            conn.commit()
            conn.close()

    def money_status(self):
        return self.money.current_amount()





