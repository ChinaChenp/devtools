from car import ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#导入过个模块
from car import Car, ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2016) 
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016) 
print(my_tesla.get_descriptive_name())