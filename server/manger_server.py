from flask import request

from website.src.product import Product


def register_routes_manager(app, executor):

    @app.post('/api/PurchaseItem')
    def api_purchase_item():
        try:
            body = request.get_json()
            item = Product.from_dict(body)
            amount = request.args.get('amount')
            if amount:
                amount = int(amount)
            executor.purchase_item(item, amount)
            return {'ok': True}, 200
        except Exception as e:
            return {'ok': False, 'message': str(e)}, 400

    @app.post('/api/ChangePrice')
    def api_change_price():
        try:
            item_id = request.args.get('item_id')
            new_price = request.args.get('new_price')
            executor.change_price(item_id, float(new_price))
            return {'ok': True}, 200
        except Exception as e:
            return {'ok': False, 'message': str(e)}, 400

    @app.get('/api/MoneyStatus')
    def api_money_status():
        data = executor.money_status()
        return {'ok': True, 'data': data}, 200