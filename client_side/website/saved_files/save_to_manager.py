from person import Person
from json_inventory import TheInventory
from product import Product
from money_manage import MoneyManage


class Manager(Person):


    _person: Person
    _inventory: TheInventory
    _item: Product
    _money: MoneyManage


    def __init__(self, person: Person, inventory: TheInventory, item: Product, money: MoneyManage):
        super().__init__(person.id, person.first_name, person.last_name, person.age,
                 person.birthday, person.phone_number, person.email)
        self.inventory = inventory
        self.item = item
        self.money = money


    @property
    def person(self):
        return self._person
    @person.setter
    def person(self, new_person):
        assert isinstance(self.person, Person)
        self.person = new_person


    @property
    def inventory(self):
        return self._inventory
    @inventory.setter
    def inventory(self, new_inventory):
        assert isinstance(self.inventory, TheInventory)
        self.inventory = new_inventory


    @property
    def item(self):
        return self.sale_item
    @item.setter
    def item(self, new_item):
        assert isinstance(self.item, Product)
        self.item = new_item


    @property
    def money(self):
        return self._money
    @money.setter
    def money(self, new_money):
        assert isinstance(self.money, MoneyManage)
        self.money = new_money



    def change_price(self, new_price):
        self.item.price = new_price


    def change_cost(self, new_cost):
        self.item.cost = new_cost


    def sale_item(self, item: Product, num: int=1):
        self.inventory.remove_item(item, num)
        self.money.add_money(item.price * num, f'from sale{item.name}')


    def bay_item(self, item: Product, num: int=1):
        self.inventory.remove_item(item, num)
        self.money.wuthdraw(item.cost * num, f'for buy{item.name}')
