from abc import ABC, abstractmethod

from product import Product


class TransactionAbc(ABC):


    @abstractmethod
    def record_sale(self, product: Product, quantity: int, sale_price: float):
        pass

    @abstractmethod
    def record_purchase(self, product: Product, quantity: int, purchase_price: float):
        pass

    @abstractmethod
    def record_return(self, product: Product, quantity: int, return_price: float):
        pass

    @abstractmethod
    def sum_profit_month(self, month: int):
        pass

    @abstractmethod
    def current_profit(self):
        pass

    @abstractmethod
    def transactions_history(self, product_id=None):
        pass

