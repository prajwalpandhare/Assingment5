class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num2 - self.num1
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num2 / self.num1

obj = Calculator(10, 94)

add_result = obj.add()
sub_result = obj.subtract()
mult_result = obj.multiply()
div_result = obj.divide()

print(add_result)
print(sub_result)
print(mult_result)
print(div_result)