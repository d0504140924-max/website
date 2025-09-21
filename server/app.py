from flask import Flask
from json_inventory import TheInventory
from website.server.inventer_server import register_routs_inv
from website.src.product import Product
from pathlib import Path


project_root = Path(__file__).resolve().parent.parent
data_dir = project_root / "data"
data_dir.mkdir(exist_ok=True)

inventory_path = data_dir / "inventory1.json"
items_path = data_dir / "items1.json"

def create_app():
    app = Flask(__name__)


    inventory = TheInventory(str(inventory_path), str(items_path))


    register_routs_inv(app, inventory)

    return app

if __name__ == "__main__":
    product = Product('p3', 'clothes', 'shirt', 'zara', 150.0, 64.0)
    inventory = TheInventory(str(inventory_path), str(items_path))
    TheInventory.add_item(inventory, product)
    app = create_app()
    app.run(debug=True, port=5000)

