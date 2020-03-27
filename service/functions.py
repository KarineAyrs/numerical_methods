import math


def two_function(x, y):  # two dim integral
    return x ** 2 + x * y + y ** 2


def function(x):
    # return math.sin(100 * x) / math.log(x + 2, math.e)
    # return x * math.exp(x * x)
    # return (math.fabs(x)) ** 3
    # return math.fabs(x)
    # return math.fabs(math.sin(1000*x))
    return 1 / (math.fabs(x) + 1)


def function1(x, y):  # y'
    # return x + y
    # return y - 2 * x / y
    # return x ** 2 - 2 * y
    # return y - 2 * x / y
    return ((x ** 2) * (y ** 2) - 2 * y) / (2 * x)
    #return y * math.tan(x) + math.sin(x)
    #return (y-4*x**3)/x
    # return (3 * y - 2 * x * y ** 2) / x
    #return -50*(y+math.cos(x))


def function2(x):
    # return math.exp(x) - x - 1
    #return math.sqrt(2 * x + 1)
    # return 3 * math.exp(-2 * x) / 4 + (x ** 2) / 2 - x / 2 + 1 / 4
    #return math.sqrt(2 * x + 1)
    return 1 / (3 * x / 2 - (x ** 2) / 2)
    #return (1-math.cos(2*x))/(4*math.cos(x))
    # return math.sqrt((4*x**2)/(16*x**2-17))  #корень из отриц числа
    #return 1 / (x / 2 + (x ** 3) / 2)
    #return -(50*(50*math.cos(x)+math.sin(x))-2500*math.exp(-50*x))/2501
