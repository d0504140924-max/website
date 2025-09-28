import sqlite3
from website.src.inventory_SQlite import TheInventory
from website.src.manager_interface import ManagerAbc
from website.src.money_SQlite import MoneyManage
from website.src.person import Person
from website.src.product import Product



class Manager(ManagerAbc):


    _db_path: str
    _inventory: TheInventory
    _money: MoneyManage

    def __init__(self, person: Person, inventory: TheInventory,
                 money: MoneyManage, db_path):
        super().__init__(person.id, person.first_name, person.last_name, person.age,
                        person.birthday, person.phone_number, person.email)
        self.db_path = db_path
        self.inventory = inventory
        self.money = money

    @property
    def db_path(self):
        return self._db_path
    @db_path.setter
    def db_path(self, new_db_path):
        assert isinstance(new_db_path, str)
        self._db_path = new_db_path

    @property
    def inventory(self):
        return self._inventory
    @inventory.setter
    def inventory(self, new_inventory):
        assert isinstance(new_inventory, TheInventory)
        self._inventory = new_inventory

    @property
    def money(self):
        return self._money
    @money.setter
    def money(self, new_money):
        assert isinstance(new_money, MoneyManage)
        self._money = new_money


    def purchase_item(self, item: Product, num: int=1):
        self.inventory.add_item(item)
        self.inventory.update_amount(item.id, num)
        self.money.withdraw(item.cost * num)

    def change_price(self, item_id: str, new_price):
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("UPDATE products SET price = ? WHERE id =?",(new_price, item_id))


    def money_status(self):
        return self.money.current_amount()





