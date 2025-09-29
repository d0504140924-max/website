from abc import ABC, abstractmethod

from person import Person


class PeopleInterface(ABC):


    @abstractmethod
    def add_user(self, person: Person):
        pass

    @abstractmethod
    def add_employee(self, person: Person):
        pass

    @abstractmethod
    def add_manager(self, person: Person):
        pass


    @abstractmethod
    def remove_person(self, person_id: str):
        pass

    @abstractmethod
    def get_person(self, person_id: str):
        pass

    @abstractmethod
    def list_people(self):
        pass



