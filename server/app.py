from flask import Flask
from manager_SQlite import Manager
from website.server.manger_server import register_routes_manager
from website.src.inventory_SQlite import TheInventory
from website.server.inventer_server import register_routes_inv
from website.src.money_SQlite import MoneyManage
from website.server.money_server import register_routes_money
from website.src.product import Product
from website.src.person import Person
from pathlib import Path


project_root = Path(__file__).resolve().parent.parent
data_dir = project_root / "data"
data_dir.mkdir(exist_ok=True)

db_path = data_dir / "main.db"


def create_app():
    app = Flask(__name__)

    p1 = Product('2345', 'clothes', 'shoe', 'nike', 300, 200)
    p2 = Product('2346', 'clothes', 'shirt', 'nike', 350, 250)
    pr1 = Person('1234567', 'david', 'rubniz', 21,
                 {'year': 2004, 'month': 6, 'day': 2})
    inventory = TheInventory(db_path)
    inventory.add_item(p1, 4)
    inventory.add_item(p2, 6)
    money = MoneyManage(db_path)
    manager = Manager(pr1, inventory, money, db_path)
    register_routes_inv(app, inventory)
    register_routes_money(app, money)
    register_routes_manager(app, manager)


    return app
if __name__ == "__main__":
    app = create_app()

    app.run(debug=True, port=5000)

