from website.config import main_url
import requests
import json
import sys

time_out = 8

def handle_response(resp):
    if resp is None:
        return
    try:
        data = resp.json()
        print('status:', resp.status_code)
        print(json.dumps(data, ensure_ascii=False, indent=3))
    except ValueError:
        print(resp.status_code, resp.text)

def posts(url, payload, parameters=None):
    try:
        return requests.post(f'{main_url}{url}', json=payload,params=parameters, timeout=time_out)
    except requests.exceptions.RequestException as e:
        print(f'post {url} error:', e)

def req_purchase_item():
    item = {
        "id": input("id: ").strip(),
        "name": input("name: ").strip(),
        "category": input("category: ").strip(),
        "manufacturer": input("manufacturer: ").strip(),
        "price": input("price: ").strip(),
        "cost": input("cost: ").strip()}
    amount = input("amount: ").strip()
    return posts('PurchaseItem', item, {'amount': amount})

def req_change_price():
    item_id = input("id: ").strip()
    new_price = input("new price: ").strip()
    parameters = {'item_id': item_id, 'new_price': new_price}
    return posts('ChangePrice', payload=None, parameters=parameters)

def req_money_status():
    try:
        return requests.get(f"{main_url}{'MoneyStatus'}",timeout=time_out)
    except requests.exceptions.RequestException as e:
        print(f'get MoneyStatus error:', e)

MENU = [
    ('purchase item', req_purchase_item),
    ('change price', req_change_price),
    ('money status', req_money_status)
]

def main():
    while True:
        print('choose from the menu: ')
        for choice, (title, _) in enumerate(MENU, start=1):
            print(f'{choice}. {title}')
        print('choose 0 for exit')
        choice = input('choice: ').strip()
        if choice == '0':
            sys.exit()
        try:
            index = int(choice) - 1
            title , function = MENU[index]
        except ValueError:
            print('invalid choice')
            continue

        print(f'-{title}-')
        activ = function()
        handle_response(activ)
if __name__ == '__main__':
    main()