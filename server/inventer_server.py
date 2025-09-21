from flask import request, jsonify, Flask
from website.src.product import Product
from website.src.json_inventory import TheInventory


class InventoryExecutor:



    _inventory: TheInventory
    _product: Product


    def __init__(self,product: Product, inventory: TheInventory):
        self.product = product
        self.inventory = inventory


    def show_inventory(self):
        return self.inventory.show_inventory()


    def show_one_category(self, category: str):
        return self.inventory.show_one_category(category)


    def show_item_details(self, id: str):
        items = self.inventory.items
        for item in items:
            if item.get('_id') == id:
                return item
        return None


    def add_item(self, commend: dict):
        try:
            item = Product.from_dict(commend)
            self.inventory.add_item(item, commend.get("num", 1))
        except Exception as e:
            raise NotImplementedError


    def remove_item(self, commend: dict):
        try:
            item = Product.from_dict(commend)
            self.inventory.remove_item(item, commend.get("num", 1))
        except Exception as e:
            raise NotImplementedError

    def get_item_amount(self, id: str):
        items = self.inventory.items
        return [p for p in items if p.get('_id') == id]

    def update_amount(self, commend: dict):
        try:
            item = Product.from_dict(commend)
            self.inventory.update_amount(item, commend.get("num", 1))
        except Exception as e:
            raise NotImplementedError

def register_routs_inv(app, executor):



    @app.get("/api/ShowAll")
    def api_shoe_all():
        data = executor.show_inventory()
        return ({'ok':True, 'data': data}),200


    @app.get("/api/Category")
    def api_category():
        category = request.args.get('category')
        if not category:
            return ({'ok': False, 'Error': 'No category specified'}), 400
        data = executor.show_one_category(category)
        return ({'ok': True, 'data': data}), 200


    @app.get("/api/ItemDetail")
    def api_item_detail():
        id = request.args.get('id')
        data = executor.show_item_details(id)
        return ({'ok':True, 'data': data}),200


    @app.post('/api/AddItem')
    def api_add_item():
        try:
            item = request.get_json(force=True) or {}
            executor.add_item(item)
            return jsonify({'ok': True}), 201
        except Exception as e:
            return jsonify({"ok": False, 'Error': str(e)}), 400


    @app.post('/api/RemoveItem')
    def api_remove_item():
        try:
            item = request.get_json(force=True) or {}
            executor.remove_item(item)
            return jsonify({'ok': True}), 201
        except Exception as e:
            return jsonify({'ok': False, 'Error': str(e)})


    @app.get('/api/GetAmount')
    def api_get_item_amount():
        id  = request.args.get("id")
        data = executor.get_item_amount(id)
        return ({"ok": True, "data":data}), 200

    @app.post('/api/UpdateAmount')
    def api_update_amount():
        id = request.args.get("id")
        data = executor.get_item_amount(id)
        data2 = executor.update_amount(data)
        return ({"ok": True, "data":data2}), 200







