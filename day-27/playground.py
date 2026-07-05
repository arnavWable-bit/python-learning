# Unlimited positional arguments

# def add(*args):
#     # print(args[1])
#     # type = tuple
#     sum = 0
#     for n in args:
#         sum += n
        
#     return sum

# total = add(1,2,3,4,5,6)
# print(total)


# Keyword Arguments

# def calculate(n, **kwargs):
#     print(kwargs)
    # print(type(kwargs))
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
        
    # print(kwargs['add'])
    
#     n += kwargs['add']
#     n *= kwargs['multiply']
#     print(n)

# calculate(2,add=3, multiply=5)



# class Car:
    
#     def __init__(self, **kw):
#         self.model = kw.get('model')
#         self.make = kw.get('make')
#         self.colour = kw.get('colour')
#         self.seats = kw.get('seats')
        

# my_car = Car()   # We are not able to see model or make inside Car() beacuse we have used **kw
# my_car = Car(make = "Nissan", model ="GT-R")
# print(my_car.model)

# my_car = Car(make = "Nissan")
# print(my_car.model)         # it will return none now because of get , previously it was returning error