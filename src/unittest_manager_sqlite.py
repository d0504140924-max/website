import unittest
from website.src.product import Product
from website.src.person import Person
from website.src.manager_SQlite import Manager
from website.src.inventory_SQlite import TheInventory
from website.src.money_SQlite import MoneyManage

class TestManager(unittest.TestCase):
    def setUp(self):
        self.inventory = TheInventory('test_manager3.db')
        self.inventory.create_table()
        self.money = MoneyManage('test_manager3.db')
        self.money.create_table()
        self.person = Person('234', 'david', 'rubniz', 21,
                             {"day":1,"month":1,"year":1995})
        self.manager = Manager(self.person,self.inventory, self.money, 'test_manager3.db')
        self.product = Product('2435', 'clothes', 'shirt', 'zara',
                               70.0, 40.0)
    def tearDown(self):
        pass

    def test_purchase_item(self):
        self.manager.purchase_item(self.product, 4)
        self.assertEqual(self.inventory.get_amount(self.product.id), 9)

        self.assertEqual(self.money.current_amount(), -4 * self.product.cost)

if __name__ == '__main__':
    unittest.main()

