class Person:
    def __init__(self, name='John Doe', age=99, phone='000'):
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
    print(Person())
    print(Person(phone='123456', age=45))
    print(Person('jancsi', 54, '312333'))
