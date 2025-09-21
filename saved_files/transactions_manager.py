from datetime import datetime
from product import Product
from transaction_abctractor import TransactionAbc

class Transaction:


    _id: str
    _type: str
    _unit_price: float
    _quantity: int
    _product: Product


    def __init__(self, id: str, type: str, unit_price: float, quantity: int=1, product: Product = None):
        self.id = id
        self.type = type
        self.unit_price = unit_price
        self.quantity = quantity
        self.product = product
        self.time = datetime.now()
        self.calculate = unit_price * quantity

    @property
    def type(self):
        return self._type
    @type.setter
    def type(self, value):
        self._type = value
        assert isinstance(value, str)
        if self.type != 'sale' and self.type != 'purchase' and self.type != 'return':
            raise ValueError('type must be either sale or purchase or return')


    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'unit_price': self.unit_price,
            'quantity': self.quantity,
            'product': self.product.name,
            'product id': self.product.id,
            'timestamp': self.time.isoformat(),
            'calculate': self.calculate,}


class TransactionsRecord(TransactionAbc, Transaction):


    def __init__(self, transactions: Transaction, list_of_transactions: list, ):
        super().__init__(transactions.id, transactions.type, transactions.unit_price,
                         transactions.quantity, transactions.product)
        self.transactions = transactions
        self.list_of_transactions = list_of_transactions
        self.list_sales = []
        self.list_purchases = []
        self.list_returns = []


    def save_transaction(self):
        if self.transactions.type == 'sale':
            sale = self.to_dict()
            self.list_sales.append(sale)
        elif self.transactions.type == 'purchase':
            purchase = self.to_dict()
            self.list_buys.append(purchase)
        elif self.transactions.type == 'return':
            _return = self.to_dict()
            self.list_returns.append(_return)
        else:
            raise NotImplementedError('')

    def record_purchase(self, ):
        pass


    def lists(self):
        self.list_of_transactions.append(self.list_sales)
        self.list_of_transactions.append(self.list_buys)




