import json
import os
from src.inventory_abstract import InventoryManage
from src.product import Product


class TheInventory(InventoryManage):

    _inventory_path: str
    _items_path: str


    def __init__(self, inventory_path, items_path):
        self.inventory_path = inventory_path
        self.items_path = items_path





    @property
    def inventory_path(self):
        return self._inventory_path
    @inventory_path.setter
    def inventory_path(self, new_path1):
        assert isinstance(new_path1, str)
        self._inventory_path = new_path1
        if not os.path.exists(new_path1):
            with open(new_path1, 'w', encoding='utf-8') as f:
                json.dump([], f)




    @property
    def items_path(self):
        return self._items_path
    @items_path.setter
    def items_path(self, new_path2):
        assert isinstance(new_path2, str)
        self._items_path = new_path2
        if not os.path.exists(new_path2):
            with open(new_path2, "w") as f:
                json.dump([], f)

    @property
    def items(self):
        return self.load_from_file(self.items_path)

    @property
    def inventory(self):
        return self.load_from_file(self.inventory_path)


    @staticmethod
    def load_from_file(path):
        try:
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
                    return data if isinstance(data, list) else []
            return []
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading file {path}: {e}")
            return []



    @staticmethod
    def save_file(path, value):
        with open(path, 'w') as json_file:
            json.dump(value, json_file)


    def get_amount(self, id_item):
        for i in self.inventory:
            if id_item.id in i:
                return id_item, i[id_item.id]
        return 0


    def add_item(self, item: Product, num=1):
        data = self.inventory
        print(data)
        print("type:", type(data))
        if not any(item.id in d for d in data):
            data.append({item.id:num})
            self.save_file(self.inventory_path, data)
        if not item.id in self.items:
            data = self.items
            data.append(item.__dict__)
            self.save_file(self.items_path, data)


    def remove_item(self, item: Product, num=1):
        if item in self.inventory:
            data = self.inventory
            data.remove(item)
            self.save_file(self.inventory_path, data)
        if item in self.items:
            data = self.items
            data.remove(item.__dict__)
            self.save_file(self.items_path, data)


    def update_amount(self, item: Product, new_amount):
        data = self.inventory
        for i in data:
            if item.id in i:
                i[item.id] = new_amount
                self.save_file(self.inventory_path, data)
            else:
                return 'no such id hes found'
        return 0


    def show_inventory(self):
        inventory = self.inventory
        items = self.items
        return inventory, items

    def show_one_category(self, category):
        the_category = self.items
        return [p for p in the_category if p.get('_category') == category]





