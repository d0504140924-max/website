import unittest
from website.src.money_SQlite import MoneyManage
from datetime import datetime
import sqlite3

class TestMoneyManageSQlite(unittest.TestCase):
    def setUp(self):
        self.table_money = MoneyManage(':memory:')
        self.table_money.create_table()

    def tearDown(self):
        self.table_money.close()

    def test_deposit_sale_purchase_withdraw(self):
        self.table_money.deposit(100.0)
        self.table_money.withdraw(40.0)
        self.table_money.purchase(70.0)
        self.table_money.sale(40.0)
        self.assertAlmostEqual(self.table_money.current_amount(), 30, places=6)

    def test_current_amount(self):
        self.table_money.deposit(100.0)
        current_amount = self.table_money.current_amount()
        self.assertEqual(current_amount, 100)

    def test_movements_record(self):
        self.table_money.time = '2025-09-01 00:00:00'
        self.table_money.deposit(100.0)
        self.table_money.time = '2025-09-10 12:00:00'
        self.table_money.deposit(200.0)
        self.table_money.time = '2025-10-01 00:00:00'
        self.table_money.deposit(300.0)
        row = self.table_money.movements_record('deposit',
                                          '2025-09-01 00:00:00',
                                          '2025-09-30 12:00:00')
        self.assertEqual(len(row), 2)


if __name__ == '__main__':
    unittest.main()