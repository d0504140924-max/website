from flask import Flask, request, jsonify
from src.product import (Product)
from src.person import Person
from src.manager_Abc import ManagerAbc
from src.json_inventory import TheInventory


class CommendExecutor:


    _person: Person
    _inventory: TheInventory
    _product: Product


    def __init__(self, person: Person, product: Product, inventory: TheInventory, manager: ManagerAbc):
        self.person = person
        self.product = product
        self.inventory = inventory
        self.manager = manager


    def execute(self, commend: dict):
        raise NotImplementedError('execute must be implemented')


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



    def change_price(self, commend: dict):
        id = commend.get('id')
        price = commend.get('price')
        try:
            self.manager.change_price(id, price)
        except Exception as e:
            raise NotImplementedError

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

    def show_money_status(self):
        pass

    def deposit_money(self, commend: dict):
        raise NotImplementedError

    def withdraw_money(self, commend: dict):
        raise NotImplementedError

    def get_item_amount(self, id: str):
        items = self.inventory.items
        return [p for p in items if p.get('_id') == id]


    def month_report(self):
        pass

    def movement_record(self):
        pass

def create_app(executor):
    app = Flask(__name__)


    @app.get("/api/Category")
    def api_category():
        category = request.args.get('category')
        if not category:
            return ({'ok':False,'Error': 'No category specified'}),400
        data = executor.show_one_category(category)
        return ({'ok':True, 'data': data}), 200


    @app.get("/api/ShoeAll")
    def api_shoe_all():
        data = executor.show_inventory()
        return ({'ok':True, 'data': data}),200


    @app.get("/api/ItemDetail")
    def api_item_detail():
        id = request.args.get('id')
        data = executor.shoe_item_details(id)
        return ({'ok':True, 'data': data}),200


    @app.post('/api/ChangePrice')
    def api_change_price():
        pass


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


    @app.get('/api/ShowMoneyStatus')
    def api_show_money_status():
        pass


    @app.post('/api/DepositMoney')
    def api_deposit_money():
        pass


    @app.post('/api/WithdrawMoney')
    def api_withdraw_money():
        pass


    @app.get('/api/GetAmount')
    def api_get_item_amount():
        id  = request.args.get("id")
        data = executor.get_item_amount()
        return ({"ok": True, "data":data}), 200


    @app.get('/api/MonthReport')
    def api_month_report():
        pass


    @app.get('/api/MovementRecord')
    def api_movement_record():
        pass




    return app
