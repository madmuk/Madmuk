class Student:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name


s = Student("John")
print(s.get_name())
s.set_name("Mike")
s.set_name("Kite")
print(s.get_name())
