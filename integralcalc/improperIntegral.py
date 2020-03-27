import math

# nesobstvenniy integral. drugoy class
def newton_method(function, num):  # p(x)=1/sqrt(1-x^2)
    x = []
    sum = 0
    for i in range(num):
        x.append(math.cos(math.pi * (2 * (i + 1) - 1) / (2 * num)))
    for i in range(num):
        sum += function(x[i])
    return sum * math.pi / num


def newton2_method(function, num):  # p(x)=sqrt(x/1-x)
    x = []
    cos = 0
    c = []
    sum = 0
    for i in range(num):
        cos = math.cos(math.pi * (2 * i - 1) / (4 * num + 2))
        x.append(cos ** 2)
    for i in range(num):
        c.append(2 * math.pi * x[i] / (2 * num + 1))
    for i in range(num):
        sum += c[i] * function(x[i])
    return sum


def newton3_method(function, num):  # p(x)=sqrt(1-x^2)
    x = []
    c = []
    sum = 0
    sin = 0
    for i in range(num):
        x.append(math.cos(math.pi * (i + 1) / (num + 1)))
    for i in range(num):
        sin = math.sin(math.pi * (i + 1) / (num + 1))
        c.append((sin ** 2) * math.pi / (num + 1))
    for i in range(num):
        sum += c[i] * function(x[i])
    return sum