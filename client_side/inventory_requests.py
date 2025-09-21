import requests
import json
import sys

base_url = "http://127.0.0.1:5000/api"
time_out = 10

def gets(path, parameters=None):
    try:
        response = requests.get(f"{base_url}{path}", params=parameters, timeout=time_out)
        return response
    except requests.exceptions.RequestException as e:
        print(f"[GET {path}] Error:", e)

def posts(path, payload=None):
    try:
        response = requests.post(f"{base_url}{path}", json=payload, timeout=time_out)
        return response
    except requests.exceptions.RequestException as e:
        print(f"[POST {path}] Error:", e)





def req_show_all():
    return gets("/ShowAll")

def req_show_one_category():
    category = input("category_name:").strip()
    return gets("/Category", parameters={"category_name": category})


def req_item_details():
    id = input("item_id:").strip()
    return gets("/ItemDetails", parameters={"item_id": id})


def req_get_amount():
    id = input("item_id:").strip()
    return gets("/GetAmount", parameters={"item_id": id})


def req_add_item():
    item = {
        "id": input("id: ").strip(),
        "name": input("name: ").strip(),
        "category": input("category: ").strip(),
        "manufacturer": input("manufacturer: ").strip(),
        "price": input("price: ").strip(),
        "cost": input("cost: ").strip()
    }
    return posts("/AddItem", item)

def req_remove_item():
    id = input("item_id:").strip()
    payload = {"item_id": id}
    return posts("/RemoveItem", payload)