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

# n  = -3
# print("positive" if n > 0 else "negative") 

# num = 9
# result = "even" if num % 2 == 0 else "odd"
# print(result)

# age = 2
# status = "adult" if age > 18 else "child"
# print(status)

# temp = -2
# result = "hot" if temp > 20 else "cold"
# print(result)

# user_role = "guest"
# acess = "full access" if user_role == "admin" else "limited acess"
# print(acess)

# methods

# name = input("enter your name: ")
# phone_number = input("enter your phone number: ")
# result=phone_number.count("-")
# result = phone_number.replace("-",(" "))
# name = len(name)

# result=name.find("a")
# result = name.rfind("i")
# result = name.upper()
# result = name.lower()
# result = name.capitalize()
# result = name.isdigit()
# result = name.isalpha()
# print(result)


# user_name = input("Enter username: ")

# if len(user_name) > 12:
#     print("your username contain more than 12 ")
# elif not user_name.find(" ") == -1:
#     print("you can't have spaces")
# elif not user_name.isalpha():
#     print("you can't have digits")
# else:
#     print(f"welcome {user_name}")    

#string indexing

# credit_number = "1234-5678-9012-3456"
# print(credit_number[0])

# print(credit_number[0:4])

# print(credit_number[5:9])

# print(credit_number[0:])

# print(credit_number[9:])

# print(credit_number[::3])

# print(credit_number[::-1])
# last_credit = credit_number[-4:]
# print(f"xxxx-xxxx-xxxx-{last_credit}")

#format specifiers

# price1 = 19223.2223798
# price2 = -1222.3355
# price3 = 2333.234567

# print(f"price1 is {price1:.2f}")
# print(f"price2 is {price2:.2f}")
# print(f"price3 is {price3:.2f}")


# print(f"price1 is {price1:10}")
# print(f"price2 is {price2:10}")
# print(f"price3 is {price3:10}")


# print(f"price1 is {price1:010}")
# print(f"price2 is {price2:010}")
# print(f"price3 is {price3:010}")


# print(f"price1 is {price1:,}")
# print(f"price2 is {price2:,}")
# print(f"price3 is {price3:,}")


# print(f"price1 is {price1:<10}")
# print(f"price2 is {price2:<10}")
# print(f"price3 is {price3:<10}")


# print(f"price1 is {price1:>10}")
# print(f"price2 is {price2:>10}")
# print(f"price3 is {price3:>10}")


# print(f"price1 is {price1:+,.2f}")
# print(f"price2 is {price2:+,.2f}")
# print(f"price3 is {price3:+,.2f}")


# print(f"price1 is {price1:^10}")
# print(f"price2 is {price2:^10}")
# print(f"price3 is {price3:^10}")

#while loop

# name = input("enter your name: ")

# while name == "":
#     print("you don't enter name")
#     name = input("enter your name: ")
# print(f"Hello {name}")


# age = int(input("enter your age: "))

# while age < 0:
#     print("you have to enter correct age")
#     age = int(input("enter your age: "))
# print(f"you are {age} years old")

# food = input("enter your food (q or quit): ")
# while not food == "q":
#     print(f"{food} is ready")
#     food = input("enter your another food (q or quit): ")
# print("bye")  

# num = int(input("enter a number between 1 - 10: "))

# while num < 1 or num > 10:
#     print("It is invalid")
#     num = int(input("enter a number between 1 - 10: "))

# print(f"your number is {num}")

# principle = 0
# rate = 0
# time = 0

# while principle <= 0:
#     principle = float(input("enter your principle: "))
#     if principle <= 0:
#         print("principle amount can't be less than zero")

# while rate <= 0:
#     rate = float(input("enter your rate: "))
#     if rate <= 0:
#         print("rate should can't be zero")

# while time <= 0:
#     time = int(input("enter time: "))
#     if time <= 0:
#         print("time can't be zero")

# total = principle * pow((1 + rate / 100), time)
# print(f"balance after {time}years/s :Rs.{total:.2f}")        

# principle = 0
# rate = 0
# time = 0

# while True:
#     principle = float(input("enter your principle: "))
#     if principle < 0:
#         print("principle amount can't be less than zero")
#     else:
#         break

# while True:
#     rate = float(input("enter your rate: "))
#     if rate < 0:
#         print("rate should can't be zero")
#     else:
#         break

# while True:
#     time = int(input("enter time: "))
#     if time < 0:
#         print("time can't be zero")
#     else:
#         break

# total = principle * pow((1 + rate / 100), time)
# print(f"balance after {time}years/s :Rs.{total:.2f}")   


    


# print("harshi : em kaavali?")
# print("bintu : sry cheppu")
# harshi = "sorry"
# while True:
#     if harshi == "sorry":
#         print("sorry bintu")
#     else:
#         break    



# num = int(input("enter a value:"))
# if num > 0:
#     print(f"{num} is positive")
# else:
#     print(f"{num} is negative")    
    

# num = int(input("enter a value:"))
# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

# n = int(input())
# print((n*(n+1)/2)

# n=int(input())
# count = 0 
# total = 0
# while count < n:
    # ..oyy emaindhaa  natural ante count 1 annam whole ante 0 nunchegaaa exactly but nenem antunna ante aa count loki em em numbers vasthunnayo chudu okasari unnavaaaaaaaaaaaaaaaaa aaaaaaaaahhhhhhh
    # print(count) #chudu 5 kooda vasthundhi oyyy anthe oka num venakki thheskuntaam hmmmmmmmmmmmmmmmmmmmmmmmmm or inko method
    # total = total + count
    # count += 1
# print(total)    #aipoindhi unnavaaaaaaaa haa annam veskoni vachale abbo chesesaava haa guuuuudd s eeroju  mind blank aipoindhi repu chesthaaa haak thinnavaaa thintunna sare thinu mari nenu anni close chesesthaaaaaaaaaaa haamm cut chesthunna ela baagundhi mai kaani...................................................................................mundhu thinu :))))))))))))))))))))))))))))hmm
# nenu oka change cheptha chey
# sum of first n whole nums anthenaaaaaa nyoo inkokati maarcahali aagu nuv manual ga rough aa first 5 whole nums ni add chey
# ex: n=3
# enti first 3 nums 012 gud ippd idhi endhulo vuntadhi e nums ae var lo ..add chese tappudu maaruthaa vuntadh igaa ha ae var..counthaaaaa
# so aa count lo em em numbers add avthunnayo print cheskoni chudu 

# for x in range(1,11):
#     print(x)

# for x in reversed(range(1,11)):
#     print(x)
# print("HAPPY BIRTHDAY")    

# credit_card = "1234-5678-8901"
# for x in credit_card:
#     print(x)

# import time
# my_time = int(input("enter your time seconds: "))

# for x in range(my_time,0,-1):
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)

#     time.sleep(1)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")

# print("TIMES UP")


#nested loop

# for x in range(3):
#     for y in range(5):
#         print("*",end="")
#     print()    

# rows = int(input("enter rows: "))
# columns = int(input("enter columns: "))
# symbol = input("enter your symbol: ")

# for x in range(rows):
#     for y in range(columns):
#         print(symbol,end="")
#     print()    


for x in range(4):
    for y in range(4):
        print("*",end="")
    print()    