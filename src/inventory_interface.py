from abc import ABC, abstractmethod
class InventoryManage(ABC):

    @abstractmethod
    def get_item_amount(self, item):
        pass


    @abstractmethod
    def add_item(self, item, num=1):
        pass


    @abstractmethod
    def remove_item(self, item):
        pass


    @abstractmethod
    def update_amount(self, item, new_amount):
        pass


    @abstractmethod
    def show_inventory(self):
        pass

