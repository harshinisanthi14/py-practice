#variables
# age=21
# print(f"your age is {age}")

# name="harshi"
# print(f"hello {name}")

# marks = 30.5
# print(f"your maarks are {marks}")

# is_number=True
# print(f"this is {is_number}")

# is_name = True
# if is_name:
#     print("your name is h")
# else:
#     print("i don't know")    


#type casting

# name="harshini"
# name1=""
# age=21
# marks=27.2
# is_there=True


# marks = int(marks)
# print(marks)

# age=float(age)
# print(age)

# name=bool(name)
# print(name)

# name1=bool(name1)
# print(name1)

#input
# name=input("enter your name: ")
# age=int(input("how old are you? "))
# age=age+1
# print(f"my name is {name}")
# print("Happy Birthday to u")
# print(f"I am {age} years old")

# length=float(input("enter the length: "))
# width=float(input("enter the width: "))
# area = length * width
# print(f"the area is {area}cm")


# item =input("enter the item: ")
# price=float(input("enter the price: "))
# quantity=int(input("how much quantity you want: "))
# total=price * quantity
# print(f"you have bought{quantity}kg's X {item}")
# print(f"the total amount is {total}")

#madlibs game
# name=input("enter the name: ")
# adjective=input("enter the adjective: ")
# verb = input("enter verb: ")
# print(f"there was a {name} lived")
# print(f"it is very {adjective}")
# print(f"it {verb} fast")


# friends=5

# friends=friends + 1
# friends += 1

# friends=friends -2
# friends -= 2

# friends=friends * 4
# friends *= 4

# friends=friends/2
# friends /= 2

# friends = friends ** 2
# friends **= 2

# friends = friends % 2
# friends %= 2

# remainder = friends % 2

# print(remainder)

#math functions

# x=3.25
# y=4
# z=8

# print(round(x))
# print(abs(y))
# print(pow(y,3))
# print(max(x,y,z))
# print(min(x,y,z))


# age = int(input("enter your age: "))
# if age>100:
#     print("you have slow to  sign up")
# elif age>18:
#     print("you r eligible for signed up")
# elif age<0:
#     print("you haven't been born yet")    
# else:
#     print("you must have 18")    

# response=input("would you have some food (y/n): ")
# if response == "y":
#     print("have some food")
# else:
#     print("no food for u")    

# name=input("enter your name: ")
# if name=="":
#     print("you dont enter u r name")
# else:
#     print(f"Hello {name}")    

# for_sale = True
# if for_sale:
#     print("the item is for sale")
# else:
#     print("the item is not for sale")    


#python calculator

# operator=input("enter a operator(+,-,*,/): ")  
# a=int(input("enter 'a' value: "))
# b=int(input("enter 'b' value: "))

# if operator == "+":
#     result = a + b
#     print(round(result))
# elif operator == "-":
#     result = a - b
#     print(round(result))
# elif operator == "*":
#     result = a * b
#     print(round(result))
# elif operator == "/":
#     result = a / b
#     print(round(result, 3))
# else:
#     print(f"{operator} is not a valid operator")        
         
#python weight converter

# weight=float(input("Enter your weight: "))
# unit=input("enter kilograms or pounds(k or l): ")

# if unit == "k":
#     weight = weight * 2.205
#     units = "lbs"
#     print(f"The weight is {round(weight, 3)} {units}")
# elif unit == "l":
#     weight = weight / 2.205
#     units = "kgs" 
#     print(f"The weight is {round(weight, 3)} {units}")

# else:
#     print(f"{unit} is not valid")

# unit = input("Enter the temperature in cesius and fahrein heat(c or f): ")
# temp = int(input("Enter the temperature: "))

# if unit == "c":
#     temp = round((9 * temp)/5 + 32, 1)
#     print(temp)
# elif unit == "f":
#     temp = round((temp - 32) * 5 / 9, 1)  
#     print(temp)
# else:
#     print(f"{unit} is not unit of measurement")     

#logical operators(or,and , not)

# temp = 70
# is_raining = False

# if temp == 25 or temp < 0 or is_raining:
#     print("It's sunny")
#     print("It is very hot")
# elif temp < 25 and temp >= 0 and not is_raining:
#     print("Its is cold")
#     print("its raining")
# elif temp >= 25 and temp <= 100:
#     print("Its warm outside")   

#conditional statement

n  = -3
print("positive" if n > 0 else "negative") 

num = 9
result = "even" if num % 2 == 0 else "odd"
print(result)

age = 2
status = "adult" if age > 18 else "child"
print(status)

temp = -2
result = "hot" if temp > 20 else "cold"
print(result)

user_role = "guest"
acess = "full access" if user_role == "admin" else "limited acess"
print(acess)