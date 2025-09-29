from flask import request
from website.src.person import Person

def register_routs_people(app, executor):

    @app.post('/api/AddUser')
    def api_add_user():
        try:
            body = request.json.get('user')
            user = Person.from_dict(body)
            executor.add_user(user)
            return {"ok": True}, 200
        except Exception as e:
            return {"ok": False, 'Error': str(e)}

    @app.post('/api/AddEmployee')
    def api_add_employee():
        try:
            body = request.json.get('employee')
            employee = Person.from_dict(body)
            executor.add_employee(employee)
            return {"ok": True}, 200
        except Exception as e:
            return {"ok": False, 'Error': str(e)}

    @app.post('/api/AddManager')
    def api_add_manager():
        try:
            body = request.json.get('manager')
            manager = Person.from_dict(body)
            executor.add_user(manager)
            return {"ok": True}, 200
        except Exception as e:
            return {"ok": False, 'Error': str(e)}

    @app.post('/api/RemovePerson')
    def api_remove_person():
        try:
            person_id = request.args.get('person_id')
            executor.remove_person(person_id)
            return {"ok": True}, 200
        except Exception as e:
            return {"ok": False, 'Error': str(e)}

    @app.get('/api/GetPerson')
    def api_get_person():
        try:
            person_id = request.args.get('person_id')
            data = executor.get_person(person_id)
            return {'ok': True,'data': data}, 200
        except Exception as e:
            return {"ok": False, 'Error': str(e)}

    @app.get('/api/ListPeople')
    def api_list_people():
        data = executor.list_people()
        return {'ok': True, 'data': data}, 200
