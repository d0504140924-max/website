from flask import request

def register_routes_money(app, executor):

    @app.get('/api/ShowMoneyStatus')
    def api_show_money_status():
        data = executor.current_amount()
        return ({'ok': True, 'data': data}), 200


    @app.post('/api/DepositMoney')
    def api_deposit_money():
        try:
            body = request.get_json(force=True) or {}
            amount = float(body.get('amount', 0))
            executor.deposit_money(float(amount))
            return {'ok': True}, 200
        except Exception as e:
            return {'ok': False, 'message': str(e)}, 400


    @app.post('/api/WithdrawMoney')
    def api_withdraw_money():
        try:
            body = request.get_json(force=True) or {}
            amount = float(body.get('amount', 0))
            executor.withdraw_money(amount)
            return {'ok': True}, 200
        except Exception as e:
            return {'ok': False, 'message': str(e)}, 400

    @app.get('/api/MonthReport')
    def api_month_report():
        try:
            month = request.args.get('month')
            year = request.args.get('year')
            data = executor.month_report(int(month), int(year))
            return {'ok': True, 'data': data}, 200
        except Exception as e:
            return {'ok': False, 'message': str(e)}, 400

    @app.get('/api/MovementsRecord')
    def api_movements_record():
        try:
            start = request.args.get('start')
            end = request.args.get('end')
            data = executor.movements_record(start=start, end=end)
            return {'ok': True, 'data': data}, 200
        except Exception as e:
            return {'ok': False, 'message': str(e)}, 400


