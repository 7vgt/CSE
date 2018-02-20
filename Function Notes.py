# Defining Functions
def hello_world():
    print("hello world!")

hello_world()


def square_it(number):
    return number ** 2


print("The Number is %d." % square_it(3))


def tip_calc(subtotal):
    tax_amt = subtotal * 0.18 # Tax_amt cannot be used outside of the def
    return tax_amt


def total_bill(bill_amt):
    total = bill_amt + tip_calc(bill_amt)
    print("Your Total Bill Is %d" % total)


total_bill(100)


def distance(x1, y1, x2, y2):
    inside = (x2 - x1) ** 2 + (y1 - y2) **2
    answer = inside ** 0.5 # This Is A Square Root
    return answer


print(distance(0, 0, 3, 4))


def pythagorean(a,b):
    inside = (a ** 2 + b ** 2)
    answer = inside ** 0.5
    return answer

print(pythagorean(5,12) )

