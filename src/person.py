

class Person:


    _first_name: str
    _last_name: str
    _age: int
    _id: str
    _phone_number: str
    _email: str


    def __init__(self, id, first_name, last_name, age,
                  phone_number=None,email=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.id = id
        self.phone_number = phone_number
        self.email = email

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, new_id):
        assert isinstance(new_id, str)
        self._id = new_id


    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, new_name):
        assert isinstance(new_name, str)
        self._first_name = new_name


    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self, new_last_name):
        assert isinstance(new_last_name, str)
        self._last_name = new_last_name


    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, new_age):
        assert isinstance(new_age, int)
        self._age = new_age


    @property
    def phone_number(self):
        return self._phone_number
    @phone_number.setter
    def phone_number(self, new_number):
        if new_number is not None:
            assert isinstance(new_number, str)
        self._phone_number = new_number


    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, new_email):
        if new_email is not None:
            assert isinstance(new_email, str)
        self._email = new_email



    @property
    def full_name(self):
        return f'{self._first_name} {self._last_name}'


    @property
    def contact_information(self):
        return f'{self._phone_number} {self._email}'


    def to_dict(self):
        return {'id':str(self.id),
                'first_name':str(self.first_name),
                'last_name':str(self.last_name),
                'age':int(self.age),
                'phone_number':str(self.phone_number),
                'email':str(self.email)}


    @classmethod
    def from_dict(cls, d: dict):
        return cls(id=str(d['id']),
                   first_name=str(d['first_name']),
                   last_name=str(d['last_name']),
                   age=int(d['age']),
                   phone_number=str(d['phone_number']),
                   email=str(d['email']))

    def __hash__(self):
        return hash(self.id)


