class Student:
    def _init_(self):
        self._name = None
        self._roll_number = None
    
    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        self._name = name
    
    def set_roll_number(self, roll_number):
        if not isinstance(roll_number, int):
            raise ValueError("Roll number must be an integer.")
        self._roll_number = roll_number
    
    def get_name(self):
        return self._name
    
    def get_roll_number(self):
        return self._roll_number
    
    def _str_(self):
        return f"Name: {self._name}, Roll Number: {self._roll_number}"

student = Student()

student.set_name("PRAJWAL")
student.set_roll_number(1234)

print(student.get_name()) 
print(student.get_roll_number())