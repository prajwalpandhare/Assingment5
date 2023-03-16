#Challenge 1: Square Numbers and Return Their Sum

class Point :
    
    def __init__(self):
        self.x=int(input("Enter first number"))
        self.y=int(input("Enter second number"))
        self.z=int(input("Enter the third number"))

    def sqSum(self):

        a=self.x**2+self.y**2+self.z**2
        return a


obj=Point()
print(obj.sqSum())
    

