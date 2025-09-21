from flask import Flask, request, jsonify
from src.manager_Abc import ManagerAbc


class MoneyExecutor:


    def change_price(self, commend: dict):
        id = commend.get('id')
        price = commend.get('price')
        try:
            self.manager.change_price(id, price)
        except Exception as e:
            raise NotImplementedError

    def show_money_status(self):
        pass

    def deposit_money(self, commend: dict):
        raise NotImplementedError

    def withdraw_money(self, commend: dict):
        raise NotImplementedError


    def month_report(self):
        pass

    def movement_record(self):
        pass

def create_app_money(executor):
    app = Flask(__name__)

    @app.post('/api/ChangePrice')
    def api_change_price():
        pass

    @app.get('/api/ShowMoneyStatus')
    def api_show_money_status():
        pass


    @app.post('/api/DepositMoney')
    def api_deposit_money():
        pass


    @app.post('/api/WithdrawMoney')
    def api_withdraw_money():
        pass

    @app.get('/api/MonthReport')
    def api_month_report():
        pass

    @app.get('/api/MovementRecord')
    def api_movement_record():
        pass

    return app