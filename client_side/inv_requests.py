import requests
import json
import sys

base_url = "http://127.0.0.1:5000/api"
time_out = 10


def handle_response(response: requests.Response):
    if response is None:
        return
    try:
        data = response.json()
        print("status:", response.status_code)
        print(json.dumps(data, ensure_ascii=False, indent=2))
    except ValueError:
        print("status:", response.status_code)
        print(response.text)


def gets(path, parameters=None):
    try:
        return requests.get(f"{base_url}{path}", params=parameters, timeout=time_out)
    except requests.exceptions.RequestException as e:
        print(f"[GET {path}] Error:", e)

def posts(path, payload=None):
    try:
        return  requests.post(f"{base_url}{path}", json=payload, timeout=time_out)
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
    amount = input("amount: ").strip()
    payload = {'item': item, 'amount': amount}
    return posts("/AddItem", payload)

def req_remove_item():
    id = input("item_id:").strip()
    payload = {"item_id": id}
    return posts("/RemoveItem", payload)


MENU = [
    ('Show inventory', req_show_all),
    ('Show one category', req_show_one_category),
    ("item's details", req_item_details),
    ('Add item', req_add_item),
    ('Remove item', req_remove_item),
    ('Item amount', req_get_amount),
]
def main():
    while True:
        print('\nchoose from the menu: ')
        for choice, (title, _) in enumerate(MENU, start=1):
            print(f"{choice}. {title}")
        print('press 0 for exit')
        choice = input('choice: ').strip()
        if choice == '0':
            print('goodbye')
            sys.exit(0)
        try:
            index = int(choice) - 1
            title, function = MENU[index]
        except (ValueError,IndexError):
            print('invalid choice')
            continue

        print(f'-{title}-')
        resp = function()
        handle_response(resp)
if __name__ == '__main__':
    main()





