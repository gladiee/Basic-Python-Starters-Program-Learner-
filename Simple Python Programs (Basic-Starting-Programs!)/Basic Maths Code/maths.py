no1 = int(input("Enter First No: "))
no2 = int(input("Enter Second NO: "))

def add():
    return no1 + no2

def sub():
    return no1 - no2

def multi():
    return no1 * no2

def div():
    return no1 / no2

sum_result = add()
print(no1, "+", no2, "=", sum_result)

subtraction_result = sub()
print(no1, "-", no2, "=", subtraction_result)

multiply_result = multi()
print(no1, "x", no2, "=", multiply_result)

divide_result = div()
print(no1, "/", no2, "=", divide_result)
