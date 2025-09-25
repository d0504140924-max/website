import unittest
import sqlite3
from website.src.product import Product
from website.src.inventory_SQlite import TheInventory

class TestTheInventorySQlite(unittest.TestCase):

    def setUp(self):
        self.inv = TheInventory(":memory:")
        self.inv.create_table()
        self.product1 = Product("2653", 'clothes','shirt', 'zara',
                               453.0, 300.0)
        self.product2 = Product("2654", 'home','sofa', 'wolmart',
                                1254, 1000)

    def tearDown(self):
        self.inv.close()

    def test_add_item(self):
        self.inv.add_item(self.product1, 32)
        self.assertEqual(self.inv.get_amount('2653'),32)
        self.inv.add_item(self.product2, 3)
        self.assertEqual(self.inv.get_amount('2654'),3)


    def test_get_amount(self):
        self.inv.add_item(self.product2, 3)
        self.inv.get_amount(self.product2.id)


    def test_show_inventory(self):
        self.inv.add_item(self.product1, 32)
        rows = self.inv.show_inventory()
        self.assertIn(('2653',32 ),rows)

    def test_show_one_category_not_found(self):
        with self.assertRaises(Exception):
            self.inv.show_one_category('toys')

    def test_show_one_category_found(self):
        self.inv.add_item(self.product2, 32)
        rows = self.inv.show_one_category('home')
        self.assertIn(('sofa', 1254.0),rows)

    def test_update_amount(self):
        self.inv.add_item(self.product2, 3)
        self.inv.update_amount(self.product2.id, +20)
        self.assertEqual(self.inv.get_amount('2654'),23)

    def test_update_amount2(self):
        self.inv.add_item(self.product2, 3)
        self.inv.update_amount(self.product2.id, -1)
        self.assertEqual(self.inv.get_amount('2654'), 2)


    def test_remove_item(self):
        self.inv.add_item(self.product1, 32)
        self.inv.remove_item(self.product1)
        self.assertIsNone(self.inv.get_amount('2654'))

if __name__ == '__main__':
    unittest.main()



