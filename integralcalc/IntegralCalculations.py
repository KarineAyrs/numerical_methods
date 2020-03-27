import math



def rectangle_method(function, begX, endX, num):
    h = (endX - begX) / num
    x = []
    x.append(0)
    sum = 0
    j = 0
    for i in range(num):
        x.append(j + h)
        j += h

    for i in range(num):
        sum += function((x[i] + x[i + 1]) / 2)
    return sum * h


def trapezoid_method(function, begX, endX, num):
    h = (endX - begX) / num
    k = []
    x = []
    j = 0
    sum = 0
    k.append(0.5)
    x.append(0)
    for i in range(num):
        x.append(j + h)
        j += h
        k.append(1)
    k[-1] = 0.5
    for i in range(num + 1):
        sum += k[i] * function(x[i])
    return sum * h


def simpsons_method(function, begX, endX, num):
    h = (endX - begX) / num
    x = []
    k = []
    j = 0
    g = 4
    x.append(j)
    k.append(1)
    k.append(4)
    sum = 0
    for i in range(num):
        x.append(j + h)
        j += h

    j = 2
    for i in range(num - 1):
        k.append(6 - k[j - 1])
        j += 1
    k[-1] = 1
    for i in range(num + 1):
        sum += k[i] * function(x[i])
    return 2 * h * sum / 6


def gaussian_method(function, begX, endX, num):
    h = (endX - begX) / num
    j = 2
    x = []
    sum = 0
    x.append(h / 2 - h / (2 * math.sqrt(3)))
    x.append((h / 2 + h / (2 * math.sqrt(3))))
    for i in range(2 * num - 2):
        x.append(x[j - 2] + h)
        j += 1
    for i in range(2 * num):
        sum += function(x[i])

    return h * sum / 2


def bode_method(function, begX, endX, num):
    # num kraten 4
    h = (endX - begX) / num
    x = []
    k = []
    sum = 0
    j = 0
    x.append(j)
    for i in range(num):
        x.append(x[j] + h)
        j += 1
    k.append(7)
    k.append(32)
    k.append(12)
    k.append(32)
    if num > 4:
        j = 4
        k.append(14)
        for i in range(num - 4):
            k.append(k[j - 3])
            j += 1
        k[-1] = 7
    else:
        k.append(7)
    for i in range(len(x)):
        sum += k[i] * function(x[i])

    return 2 * h * sum / 45


def ueddel_method(function, begX, endX, num):
    h = (endX - begX) / num
    x = []
    k = []
    sum = 0
    j = 0
    x.append(j)
    for i in range(num):
        x.append(x[j] + h)
        j += 1
    k.append(1)

    k.append(5)
    k.append(1)
    k.append(6)
    k.append(1)
    k.append(5)
    if num > 6:
        j = 6
        k.append(2)
        for i in range(num - 6):
            k.append(k[j - 5])
            j += 1
        k[-1] = 1
    else:
        k.append(1)
    for i in range(len(x)):
        sum += k[i] * function(x[i])
    return 3 * h * sum / 10


def no_name_method(function, begX, endX, num):
    h = (endX - begX) / num
    x = []
    k = []
    sum = 0
    j = 0
    x.append(j)
    for i in range(num):
        x.append(x[j] + h)
        j += 1
    k.append(41)

    k.append(216)
    k.append(27)
    k.append(272)
    k.append(27)
    k.append(216)
    if num > 6:
        j = 6
        k.append(82)
        for i in range(num - 6):
            k.append(k[j - 5])
            j += 1
        k[-1] = 41
    else:
        k.append(41)
    for i in range(len(x)):
        sum += k[i] * function(x[i])
    return h * sum / 140