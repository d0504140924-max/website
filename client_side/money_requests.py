import requests
import json
import sys


main_url = 'http://127.0.0.1:5000/api/'
time_out = 9

def handle_response(resp: requests.Response):
    if resp is None:
        return
    try:
        data = resp.json()
        print('status:', resp.status_code)
        print(json.dumps(data, ensure_ascii=False, indent=2))
    except ValueError:
        print('status:', resp.status_code)
        print(resp.text)

def gets(url: str, parameters=None):
    try:
        return requests.get(f'{main_url}{url}', params=parameters, timeout=time_out)
    except requests.exceptions.RequestException as e:
        print(f'GET {url} error:', e)

def posts(url: str, payload=None):
    try:
        return requests.post(f'{main_url}{url}', json=payload, timeout=time_out)
    except requests.exceptions.RequestException as e:
        print(f'POST {url} error:', e)


def req_show_money_status():
    return gets('ShowMoneyStatus')

def req_deposit_money():
    amount = input('amount:').strip()
    payload = {'amount': amount}
    return posts('Deposit', payload)

def req_withdraw_money():
    amount = input('amount:').strip()
    payload = {'amount': amount}
    return posts('Withdraw', payload)

def req_month_report():
    month = input('month:').strip()
    year = input('year:').strip()
    payload = {'month': month, 'year': year}
    return gets('MovementRecord', payload)

def req_movements_record():
    type = input('type:').strip()
    start = input('start:').strip()
    end = input('end:').strip()
    payload = {'type': type, 'start': start, 'end': end}
    return gets('MovementsRecord', payload)


MENU = [
    ('show money status', req_show_money_status),
    ('deposit money', req_deposit_money),
    ('withdraw money', req_withdraw_money),
    ('month report', req_month_report),
    ('move report', req_movements_record)]

def main():
    while True:
        print('choose from menu: ')
        for choice, (title, _) in enumerate(MENU, start=1):
            print(f"{choice}. {title}")
        print('press 0 for exit')
        choice = input('choice: ').strip()
        if choice == '0':
            print('goodbye')
            sys.exit(0)
        try:
            index = int(choice) - 1
            title,function = MENU[index]
        except (ValueError, IndexError):
            print('invalid choice:')
            continue

        print(f'-{title}-')
        active = function()
        handle_response(active)

if __name__ == '__main__':
    main()



