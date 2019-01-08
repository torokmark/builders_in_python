class PersonBuilder:
    def __init__(self):
        self._name = 'John Doe'
        self._age = 99
        self._phone = '000'

    def name(self, name):
        self._name = name
        return self

    def age(self, age):
        self._age = age
        return self

    def phone(self, phone):
        self._phone = phone
        return self

    def build(self):
        return Person(self._name, self._age, self._phone)

class Person:
    def __init__(self, name, age, phone):
        self._name = name
        self._age = age
        self._phone = phone

    def name(self):
        return self._name

    def age(self):
        return self._age
    
    def phone(self):
        return self._phone

    def __str__(self):
        return '[name={}; age={}; phone={}]'.format(self._name, self._age, self._phone)

if __name__ == '__main__':
    print(PersonBuilder().name('jancsi').age(12).phone('11223344').age(18).build())
    print(PersonBuilder().age(12).phone('11223344').age(18).build())
    print(PersonBuilder().build())
