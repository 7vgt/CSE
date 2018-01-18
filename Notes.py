# print("Hello World")
#
# #Andrew Esparza
# #this is python 2.7
#
# a=4
# b=3
#
# print(3 + 5)
# print(5 - 3)
# print(3 * 5)
# print(6 / 2)
# print(3 ** 2)
#
# print()# this makes a new line. In python 3.6,it looks like: print()
# print("see if you can figure this out")
# print(14%5) # this is time 12 is the modulies #its like a mixed fraction, but the whole numbers are gone now and the denominater
#
# car_name= "weibe moble"
# car_type= "Tesla"
# car_cylinders= 8
# car_mgp=9000.1
#
# #Inline printing
# print("I have a car called the %s"% car_name)   #%s string
# print("I have a car called the %s").It's a%s" % (car_name, car_type))
#
# #asking for imput
# name = input("what is your name?")
# print("hello %s," % name)
# Age = input("how old are you?")
# print("%s?! wow, you are really old!") % Age

#function

"""
def print_hw():
    print("hello world")


print_hw()
print_hw()
print_hw()

def say_hi(name):
    print("hello %s." %name)
    print("enjoy your day.")

say_hi("john")


def print_age(name,age):
    print("%s is %d years old." %(name, age))
    age = age + 1 #age = age + 1
    print("Next year, they will be %d" % age)


print_age("john", 15)


def f(x):
    return x**3+4*x**2+7*x-4


print(f(3))
print(f(4))
print(f(5))





#if statements


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80 :
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >=60:
        return "D"
    elif percentage >=50:
        return "F"
    elif percentage >=40:
        return "F"
    elif percentage >=30:
        return "F"
    elif percentage >=20:
        return "F"
    elif percentage >=10:
        return "F"
    elif percentage >=0:
        return "NA"


def happy_bday(name):
    print("Happy birthday to you" + ",")
    print("Happy birthday to you" + ",")
    print("Happy birthday dear %s," % name)
    print("Happy birthday to you" + ".")


happy_bday("John")


# Loops

for num in range(100):
    print(num + 1)


a = 1
while a < 10:
    print(a)
    a += 1


#random numbers
import random   # This shoulkd be on line 1
print(random.randint(0,100))

#comparisons
print(1==1) #is1 equal to 1
print(1!=2) # is 1 not eqaul to 2?
print(10 <=15)
print(not False)



#recasting

c = '1'
print(c ==1)
print(int (c) == 1)  #both are ints
print(c == str(1))  #both are strings

# input command ALWAYS gives a string

#generat random number first for project
# Second take an input (number) from the user
#third compare input to generate number
#fourth add higher and lower statements
#fitfth add 5 guesse

# Notes 1/18/2018
"""
# list

the_count = [1, 2, 3, 4, 5]
shopping_list = ["noodles", "Eggrolls","Milk", "Rice","soda"]

print(shopping_list[2])

print(len(shopping_list))

# going through a list

for item in shopping_list:
    print(item)

for num in the_count:
    print(num*2)

len(shopping_list)   # gives me the length of the shopping list
range(3)  # gives a list of numbers 0 through 2
range(len(shopping_list))  # A LIST OF EVERY INDEX IN A LIST


for num in range(len(shopping_list)):
    item = shopping_list[num]
    print("The item at index %d is %s" % (num, item))


# turns into a list
str1 = "Hello class!"
listOne = list(str1)
print(listOne)
listOne[11] = '.'
print(listOne)
print("".join(listOne))

