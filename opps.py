#initiate a class 

class employee:
    ##dunder methos , magic method , constructor method 
    def __init__(self):
        self.age = 25 
        self.address = "Pune"
        self.salary= 10000000


    def travel(self,destination):
        print(f"i am travelling{destination}")




sam=employee()
sam.travel("kashmir")
#print(sam.salary)


