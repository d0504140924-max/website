from website.config import main_url
import requests
import json

time_out = 10

def handle_response(resp):
    if resp is None:
        return
    try:
        data = resp.json()
        print('status_code:', resp.status_code)
        print(json.dumps(data,ensure_ascii=False, indent=4))
    except requests.exceptions.RequestException:
        print('status_code:', resp.status_code)
        print(resp.text)

def posts(path, payload=None, parameters=None):
    try:
        return requests.post(f"{main_url}{path}", json=payload, params=parameters, timeout=time_out)
    except requests.exceptions.RequestException as e:
        print(f"[POST {path}] Error:", str(e))

def gets(path, parameters=None):
    try:
        return requests.get(f'{main_url}{path}', params=parameters, timeout= time_out)
    except requests.exceptions.RequestException as e:
        print(f'[GET {path}] error:', str(e))

def req_add_user():
    user = {
        'id': input('person_id: ').strip(),
        'first_name': input('first_name: ').strip(),
        'last_name': input('last_name: ').strip(),
        'age': int(input('age: ').strip()),
        'phone_number': input('phone_number: ').strip(),
        'email': input('email: ').strip()
    }
    return posts('AddUser', payload={'user': user})

def req_add_employee():
    employee = {
        'id': input('person_id: ').strip(),
        'first_name': input('first_name: ').strip(),
        'last_name': input('last_name: ').strip(),
        'age': int(input('age: ').strip()),
        'phone_number': input('phone_number: ').strip(),
        'email': input('email: ').strip()
    }
    return posts('AddEmployee', {'employee': employee})

def req_add_manager():
    manager = {
        'id': input('person_id: ').strip(),
        'first_name': input('first_name: ').strip(),
        'last_name': input('last_name: ').strip(),
        'age': int(input('age:').strip()),
        'phone_number': input('phone_number: ').strip(),
        'email': input('email: ').strip()
    }
    return posts('AddManager', {'manager': manager})

def req_remove_person():
    person_id = input('person_id: ').strip()
    return posts('RemovePerson', parameters=person_id)

def req_get_person():
    person_id = input('person_id: ').strip()
    return gets('GetPerson', person_id)

def req_list_people():
    return gets('ListPeople')
