import json
import os


class Product:


    _id: str
    _category: str
    _name: str
    _manufacturer:str
    _price: float
    _cost: float


    def __init__(self, id, category, name, manufacturer, price, cost):
        self.id = id
        self.category = category
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.cost = cost



    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, new_id):
        assert isinstance(new_id, str)
        self._id = new_id


    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, new_category):
        assert isinstance(new_category, str)
        self._category = new_category


    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        assert isinstance(new_name, str)
        self._name = new_name


    @property
    def manufacturer(self):
        return self._manufacturer
    @manufacturer.setter
    def manufacturer(self, new_manufacturer):
        assert isinstance(new_manufacturer, str)
        self._manufacturer = new_manufacturer


    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, new_price):
        assert isinstance(new_price, (float, int))
        self._price = new_price


    @property
    def cost(self):
        return self._cost
    @cost.setter
    def cost(self, new_cost):
        assert isinstance(new_cost, (float, int))
        self._cost = new_cost


    def to_dict(self):
        return {'id':str(self.id),
                'category':str(self.category),
                'name':str(self.name),
                'manufacturer':str(self.manufacturer),
                'price':float(self.price),
                'cost':float(self.cost)}


    @classmethod
    def from_dict(cls, d: dict):
        return cls(id=str(d['id']),
                   category=str(d['category']),
                   name=str(d['name']),
                   manufacturer=str(d['manufactory']),
                   price=float(d['price']),
                   cost=float(d['cost']))

    def __hash__(self):
        return hash(self.id)


    def __eq__(self, other):
        if isinstance(other, Product):
            return self.id == other.id
        return False


    def __hash__(self):
        return hash(self.id)
