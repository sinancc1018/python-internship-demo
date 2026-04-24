# def areaofcircle():
#     radius = int(input("Enter The radius of circle:  "))
#     area = 3.14*(radius**2)
#     print(area)

# areaofcircle()

# def areaofcircle(r):
#     area = 3.14*(r**2)
#     return area,r

# result , radius= areaofcircle(int(input("Enter the radius of circle: ")))

# print("radius of the circle",radius)
# print("Area of tghe circle",result)


# add = lambda num: num + 10
# print("Sum :", add(5))

# product = lambda a,b: a * b
# print("Product :", product(3,5))

# isEven = lambda num: "Even" if num % 2 == 0 else "Odd"

# print(isEven(int(input("Enter a number: "))))


#FOR LOOP
"""orders = [1200, 4000, 200, 5000]

for order in orders:
    tax = order * 10/100
    print(f"Order amount: {order}, Tax: {tax}")

"""
# count = 2
# while count <= 20 :
#         print(count)
#         count = count + 2


# #OOP CORE
# class Student:
#     def __init__(self, rno, name, course):
#         self.rno = rno
#         self.name = name
#         self.course = course
    
#     def display_info(self):
#         print(f"Roll No: {self.rno}")
#         print(f"Name: {self.name}")
#         print(f"Course: {self.course}")

# s1 = Student(1, "Sinan", "Cs")
# s1.display_info()
# print()

# s2 = Student(2, "Sijas", "Cs")
# s2.display_info()
# print()

# s2 = Student(3, "Salman", "Cs")
# s2.display_info()
# print()

# INHERITANCE

# class Product:
#     def __init__(self, id, title, price):
#         self.id = id
#         self.title = title
#         self.price = price

#     def display(self):
#         print(f"ID: {self.id}")
#         print(f"Title: {self.title}")
#         print(f"Price: {self.price}")


# class ElectronicProduct(Product):
#     def __init__(self, id, title, price, warranty, manufacture):
#         super().__init__(id, title, price)
#         self.warranty = warranty
#         self.manufacture = manufacture

#     def display(self):
#         super().display()  
#         print(f"Warranty: {self.warranty} years")
#         print(f"Manufacture: {self.manufacture}")


# prod1 = ElectronicProduct(1, "Oppo", 7899, 4, "Oppo")
# prod1.display()

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self,amt):
        self.balance = self.balance + amt
    def withdraw(self,amt):
        if amt > self.balance:
            print("Insufficient balance")
        self.balance = self.balance - amt
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")


acc = BankAccount("Sinan", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.display_info()