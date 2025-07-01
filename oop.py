class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    @staticmethod
    def genral():
        return "Car are means of transport"     

class Electriccar(Car):
    def __init__(self,model,brand,battary_size):
        super().__init__(brand,model)
        self.battary_size = battary_size   

my_tesla_car = Electriccar("Tesla","Model S","85kwh")
print(isinstance(my_tesla_car,Car))
print(isinstance(my_tesla_car,Electriccar))
print(my_tesla_car.brand)
print(my_tesla_car.model)   
print(my_tesla_car.battary_size)                

my_car = Car("Toyota","Fortuner")
print(my_car.brand)
print(my_car.model) 


my_new_car = Car("Tata","safari")
print(my_new_car.brand)
print(my_new_car.model) 
print(Car.genral()) 
    
# multiple inheritence

class Battry:
    def Battry_info(self):
        return "This is battry"

class engine:
    def engine_info(self):
        return "This is engine"

class Electriccartwo(Battry,engine,Car):
    pass

my_new_tesla = Electriccartwo("Tesla","Model s")
print(my_new_tesla.engine_info())    
print(my_new_tesla.Battry_info())