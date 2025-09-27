from flask import request, jsonify



def register_routes_inv(app, executor):



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
        data = executor.get_item_by_id(id)
        return ({'ok':True, 'data': data}),200


    @app.post('/api/AddItem')
    def api_add_item():
        try:
            item = request.get_json(force=True) or {}
            number = request.args.get('number')
            if not number is None:
                number = int(number)
            executor.add_item(item, number)
            return jsonify({'ok': True}), 201
        except Exception as e:
            return jsonify({"ok": False, 'Error': str(e)}), 400


    @app.post('/api/RemoveItem')
    def api_remove_item():
        try:
            item = request.args.get('item_id')
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
        try:
            id = request.args.get("id")
            new_amount = request.args.get("new_amount")
            executor.get_item_amount(id, new_amount)
            return {"ok": True}, 200
        except Exception as e:
            return jsonify({"ok": False, 'Error': str(e)}), 400






