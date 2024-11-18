
#prosedural programming
#object oriented way of programming(oops)

#class->blueprint of object
#object->instance of a class

#in a class we have attribute and methods
#two types of attributes
#1.class attribute ->variable created inside a class
#2.instance attribute ->unique for each object

#any function created inside a class is called method
#every method 1st argument will be self
#constructor ->its a method which is called when you create an object

class Car:
    material='steel'
    wheels=4
    #initilization of calss /contructor
    def __init__(self,color,fuel,category):
        self.color=color
        self.build=category
        self.fuel=fuel
    
    def get_car_color_build(self):
        return f"car is {self.color} {self.build}"



car1=Car('blue','petrol','sedan')
car2=Car('black','cng','suv')

print(car2.color)
print(car1.color)

print(car2.get_car_color_build())


class Book:
    paper='wooden'

    def __init__(self,title, author, price, quantity):
        self.title=title
        self.author=author
        self.price=price
        self.quantity=quantity
    def __str__(self):
        return self.author
    
    def get_price(self):
        return self.price
    
my_book = Book(title="1984", author="George Orwell", price=29.99, quantity=100)

# Get and set price
print(my_book.get_price())  # Output: 29.99
print(my_book.price)

print(my_book)
class Circle:
    Pi=3.14

    def __str__(self):
        return f"circle with radius {self.radius}"

    def __init__(self,r):
        self.radius=r
    

    def area(self):
        return self.Pi*(self.radius**2)
    
    def circumference(self):
        return 2*self.Pi*self.radius
    
obj1=Circle(10)
print(obj1.area())

print(obj1)



class broker:
    stock_prices={'amzn':500,'goog':600,'tsla':900}

    def __init__(self,name,id,money):
        self.name=name
        self.id=id
        self.wallet=money
        self.porfolio={}
    
    def __str__(self):
        return f"{self.name} and {self.id}"

    def buy(self,name):
        found=self.stock_prices.get(name)
        if found:
            if self.wallet>found:
                self.porfolio.update({name:found})
                self.wallet=self.wallet-found
            else:
                print('you dont have enough money')
                return 'you dont have enough money'
        else:
            print('this stock doesnt exist')
            return 'this stock doesnt exist'

    def sell(self,name):
        found=self.porfolio.get(name)
        if found:
            
            self.porfolio.pop(name)
            self.wallet=self.wallet+found
        
        else:
            return 'this stock doesnt exist'

user1=broker('matt',123,1000)
print(user1.porfolio)
user1.buy('goog')
broker.buy(user1,'goog')
user1.buy('amzn')
print(user1.porfolio)
user1.sell('goog')
print(user1.porfolio)