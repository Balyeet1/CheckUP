from typing import Optional


class User:
    def __init__(self, id: Optional[int] = None, username: Optional[str] = None, first_name: Optional[str] = None,
                 last_name: Optional[str] = None, age: Optional[int] = None, date_of_birth: Optional[str] = None,
                 external_id: Optional[str] = None, created_at: Optional[str] = None, **kwargs):
        self.id = id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.date_of_birth = date_of_birth
        self.external_id = external_id
        self.created_at = created_at

    def get_id(self):
        return self.id

    def get_username(self):
        return self.username

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_age(self):
        return self.age

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_external_id(self):
        return self.external_id

    def get_created_at(self):
        return self.created_at

    def __str__(self):
        return '\n'.join(f'{key}: {value}' for key, value in self.__dict__.items())
