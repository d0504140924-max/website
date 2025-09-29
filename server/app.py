from flask import Flask
from manager_SQlite import Manager
from website.server.manger_server import register_routes_manager
from website.src.inventory_SQlite import TheInventory
from website.server.inventory_server import register_routes_inv
from website.src.money_SQlite import MoneyManage
from website.server.money_server import register_routes_money
from website.src.person import Person
from website.src.people_SQlite import People
from website.server.people_server import register_routs_people
from website.config import DB_PATH_STR, DEBUG, PORT, HOST

inventory = TheInventory(DB_PATH_STR)
money = MoneyManage(DB_PATH_STR)
pr1 = Person('1234567', 'david', 'rubniz', 21)
manager = Manager(pr1, inventory, money, DB_PATH_STR)
people = People(DB_PATH_STR, pr1)

def create_app():
    app = Flask(__name__)


    register_routes_inv(app, inventory)
    register_routes_money(app, money)
    register_routes_manager(app, manager)
    register_routs_people(app, people)


    return app
if __name__ == "__main__":
    app = create_app()
    money.create_table()
    inventory.create_table()
    people.create_table()
    app.run(debug=DEBUG, host=HOST, port=PORT)

