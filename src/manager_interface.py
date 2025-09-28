from abc import ABC, abstractmethod
from website.src.product import Product
from website.src.person import Person

class ManagerAbc(ABC, Person ):



    @abstractmethod
    def purchase_item(self, item: dict, num: int=1):
        pass

    @abstractmethod
    def change_price(self, item_id: str, new_price):
        pass

    @abstractmethod
    def money_status(self):
        pass


