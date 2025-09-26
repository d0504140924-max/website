from abc import ABC, abstractmethod
from product import Product
from website.src.person import Person

class ManagerAbc(ABC, Person ):


    @abstractmethod
    def change_price(self, item: Product, new_price):
        pass

    @abstractmethod
    def purchase_item(self, item: Product, num: int=1):
        pass

    @abstractmethod
    def money_status(self):
        pass


