def eulerian_method(function1, function2, beg, end, x0, y0, num):
    x = []
    y = []
    h = (end - beg) / num
    yt = []
    x.append(x0)
    y.append(y0)
    for i in range(num - 1):
        x.append(x[i] + h)
        y.append(y[i] + function1(x[i], y[i]) * h)
    for i in range(num):
        yt.append(function2(x[i],))
    return x, y, yt


def eulerian_modified_method(function1, function2, beg, end, x0, y0, num):
    x = []
    y = []
    h = (end - beg) / num
    yt = []
    x.append(x0)
    y.append(y0)
    for i in range(num - 1):
        k = function1(x[i], y[i]) * h
        x.append(x[i] + h)
        y.append(y[i] + h * function1(x[i] + h / 2, y[i] + k / 2))
    for i in range(num):
        yt.append(function2(x[i]))
    return x, y, yt


def eulerian_fourth_method(function1, function2, beg, end, x0, y0, num):
    x = []
    y = []
    h = (end - beg) / num
    yt = []
    x.append(x0)
    y.append(y0)
    for i in range(num - 1):
        k1 = function1(x[i], y[i]) * h
        k2 = function1(x[i] + h / 2, y[i] + k1 / 2) * h
        k3 = function1(x[i] + h / 2, y[i] + k2 / 2) * h
        k4 = function1(x[i] + h, y[i] + k3) * h
        x.append(x[i] + h)
        y.append(y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)
    for i in range(num):
        yt.append(function2(x[i]))
    return x, y, yt


def runge_kutta_second_grade(function1, function2, beg, end, x0, y0, num, C2):
    x = []
    y = []
    h = (end - beg) / num
    yt = []
    alpha = 1 / (2 * C2)
    C1 = 1 - C2
    x.append(x0)
    y.append(y0)
    k1 = []
    k2 = []
    for i in range(num - 1):
        k1.append(function1(x[i], y[i]) * h)
        k2.append(function1(x[i] + alpha * h, y[i] + alpha * k1[i]) * h)
        x.append(x[i] + h)
        y.append(y[i] + C1 * k1[i] + C2 * k2[i])
    for i in range(num):
        yt.append(function2(x[i]))
    return x, y, yt



def runge_kutta_third_grade(function1, function2, beg, end, x0, y0, num, alpha2, alpha3):
    x = []
    y = []
    yt = []
    h = (end - beg) / num
    x.append(x0)
    y.append(y0)
    C2 = (alpha3 / 2 - 1 / 3) / (alpha2 * (alpha2 - alpha3))
    C3 = (1 / 2 - C2 * alpha2) / alpha3
    b21 = alpha2
    b32 = 1 / (6 * alpha2 * C3)
    b31 = alpha3 - b32
    C1 = 1 - C2 - C3
    for i in range(num - 1):
        k1 = function1(x[i], y[i]) * h
        k2 = function1(x[i] + alpha2 * h, y[i] + b21 * k1) * h
        k3 = function1(x[i] + alpha3 * h, y[i] + b31 * k1 + b32 * k2) * h
        x.append(x[i] + h)
        y.append(y[i] + C1 * k1 + C2 * k2 + C3 * k3)
    for i in range(num):
        yt.append(function2(x[i]))
    return x, y, yt


def runge_kutta_fourth_grade(function1, function2, beg, end, x0, y0, num, alpha2, alpha3, alpha4):
    if alpha2 * alpha3 * alpha4 * (alpha3 - alpha2) * (alpha4 - alpha2) * (alpha4 - alpha3) != 0:
        alpha4 = 1
        h = (end - beg) / num
        C2 = (2 * alpha3 - 1) / (12 * alpha2 * (alpha3 - alpha2) * (1 - alpha3))
        C4 = (6 * alpha2 * alpha3 - 4 * alpha2 - 4 * alpha3 + 3) / (12 * (1 - alpha2) * (1 - alpha3))
        b42 = (4 * alpha3 ** 2 - alpha2 - 5 * alpha3 + 2) / (24 * C4 * alpha3 * (alpha3 - alpha2))
        C3 = (1 - 2 * alpha2) / (12 * alpha3 * (1 - alpha2) * (1 - alpha3))
        b43 = (1 - 2 * alpha2) / (24 * C4 * alpha3 * (alpha3 - alpha2))
        b41 = 1 - b42 - b43
        b21 = alpha2
        b32 = 1 / (24 * C4 * b43 * alpha2)
        b31 = alpha3 - b32
        C1 = 1 - C2 - C3 - C4
        y = []
        yt = []
        x = []
        x.append(x0)
        y.append(y0)
        for i in range(num - 1):
            k1 = function1(x[i], y[i]) * h
            k2 = function1(x[i] + alpha2 * h, y[i] + b21 * k1) * h
            k3 = function1(x[i] + alpha3 * h, y[i] + b31 * k1 + b32 * k2) * h
            k4 = function1(x[i] + alpha4 * h, y[i] + b41 * k1 + b42 * k2 + b43 * k3) * h
            x.append(x[i] + h)
            y.append(y[i] + C1 * k1 + C2 * k2 + C3 * k3 + C4 * k4)
        for i in range(num):
            yt.append(function2(x[i]))
        return x, y, yt
    return 0, 0, 0


def runge_kutta_fourth_grade_delta_zero1(function1, function2, beg, end, x0, y0, num, C3):
    alpha2 = 1 / 2
    alpha3 = 0
    alpha4 = 1
    if alpha2 * alpha3 * alpha4 * (alpha3 - alpha2) * (alpha4 - alpha2) * (alpha4 - alpha3) == 0:
        h = (end - beg) / num
        C2 = 2 / 3
        C4 = 1 / 6
        b42 = 3 / 2
        b43 = 6 * C3
        b41 = -1 / 2 - 6 * C3
        b21 = 1 / 2
        b32 = 1 / (12 * C3)
        b31 = -1 / (12 * C3)
        C1 = 1 / 6 - C3
        y = []
        yt = []
        x = []
        x.append(x0)
        y.append(y0)
        for i in range(num - 1):
            k1 = function1(x[i], y[i]) * h
            k2 = function1(x[i] + alpha2 * h, y[i] + b21 * k1) * h
            k3 = function1(x[i] + alpha3 * h, y[i] + b31 * k1 + b32 * k2) * h
            k4 = function1(x[i] + alpha4 * h, y[i] + b41 * k1 + b42 * k2 + b43 * k3) * h
            x.append(x[i] + h)
            y.append(y[i] + C1 * k1 + C2 * k2 + C3 * k3 + C4 * k4)
        for i in range(num):
            yt.append(function2(x[i]))
        return x, y, yt
    else:
        return 0, 0, 0


def runge_kutta_fourth_grade_delta_zero2(function1, function2, beg, end, x0, y0, num, C3):
    alpha2 = 1 / 2
    alpha3 = 1 / 2
    alpha4 = 1
    if alpha2 * alpha3 * alpha4 * (alpha3 - alpha2) * (alpha4 - alpha2) * (alpha4 - alpha3) == 0:
        h = (end - beg) / num
        C2 = 2 / 3 - C3
        C4 = 1 / 6
        b42 = 1 - 3 * C2
        b43 = 3 * C3
        b41 = 0
        b21 = 1 / 2
        b32 = 1 / (6 * C3)
        b31 = 1 / 2 - 1 / (6 * C3)
        C1 = 1 / 6
        y = []
        yt = []
        x = []
        x.append(x0)
        y.append(y0)
        for i in range(num - 1):
            k1 = function1(x[i], y[i]) * h
            k2 = function1(x[i] + alpha2 * h, y[i] + b21 * k1) * h
            k3 = function1(x[i] + alpha3 * h, y[i] + b31 * k1 + b32 * k2) * h
            k4 = function1(x[i] + alpha4 * h, y[i] + b41 * k1 + b42 * k2 + b43 * k3) * h
            x.append(x[i] + h)
            y.append(y[i] + C1 * k1 + C2 * k2 + C3 * k3 + C4 * k4)
        for i in range(num):
            yt.append(function2(x[i]))
        return x, y, yt
    else:
        return 0, 0, 0


def runge_kutta_fourth_grade_delta_zero3(function1, function2, beg, end, x0, y0, num, C4):
    alpha2 = 1
    alpha3 = 1 / 2
    alpha4 = 1
    if alpha2 * alpha3 * alpha4 * (alpha3 - alpha2) * (alpha4 - alpha2) * (alpha4 - alpha3) == 0:
        h = (end - beg) / num
        C2 = 1 / 6 - C4
        C3 = 2 / 3
        b42 = -1 / (6 * C4)
        b43 = 1 / (3 * C4)
        b41 = 1 - 1 / (6 * C4)
        b21 = 1
        b32 = 1 / 8
        b31 = 3 / 8
        C1 = 1 / 6
        y = []
        yt = []
        x = []
        x.append(x0)
        y.append(y0)
        for i in range(num - 1):
            k1 = function1(x[i], y[i]) * h
            k2 = function1(x[i] + alpha2 * h, y[i] + b21 * k1) * h
            k3 = function1(x[i] + alpha3 * h, y[i] + b31 * k1 + b32 * k2) * h
            k4 = function1(x[i] + alpha4 * h, y[i] + b41 * k1 + b42 * k2 + b43 * k3) * h
            x.append(x[i] + h)
            y.append(y[i] + C1 * k1 + C2 * k2 + C3 * k3 + C4 * k4)
        for i in range(num):
            yt.append(function2(x[i]))
        return x, y, yt
    else:
        return 0, 0, 0


def adams_third_grade(function1, function2, beg, end, xn, yn, num):
    h = (end - beg) / num
    y = yn
    x = xn
    yt = []
    for i in range(num - 3):
        y.append(y[-1] + h * (23 * function1(x[-1], y[-1]) / 12 - 4 * function1(x[-2], y[-2]) / 3 +
                              5 * function1(x[-3], y[-3]) / 12))
        x.append(x[i + 2] + h)
    for i in range(num):
        yt.append(function2(x[i]))
    return x, y, yt


def adams_fourth_grade(function1, function2, beg, end, xn, yn, num):
    h = (end - beg) / num
    y = yn
    x = xn
    yt = []
    for i in range(num - 4):
        y.append(y[-1] + h * (55 * function1(x[-1], y[-1])/24 - 59 * function1(x[-2], y[-2])/24 +
                              37 * function1(x[-3], y[-3])/24
                              - 3 * function1(x[-4], y[-4])/24))
        x.append(x[i + 2] + h)
    for i in range(num):
        yt.append(function2(x[i]))

    return x, y, yt
