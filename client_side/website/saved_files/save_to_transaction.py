@property
    def id(self):
        return self._id
    @id.setter
    def id(self, new_id):
        assert isinstance(new_id, str)
        self.id = new_id

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, mew_type):
        assert isinstance(new_type, str)
        self.type = new_type

    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        assert isinstance(unit_price, float)
        self._unit_price = unit_price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        assert isinstance(quantity, int)
        self._quantity = quantity

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, new_product):
        assert isinstance(new_product, Product)
        self._product = new_product
