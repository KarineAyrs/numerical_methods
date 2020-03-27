import diffequations.diff_equations as df
import service.servicefunctions as sf


def eulerian_first_grade_method(functions1, functions2, beg, end, y10, y20, num, eps=None):
    if eps == None:
        x, y1, y2, y1r, y2r = [], [], [], [], []
        h = (end - beg) / num
        x.append(beg)
        y1.append(y10)
        y2.append(y20)

        for i in range(num - 1):
            x.append(x[i] + h)
            y1.append(y1[i] + h * functions1(y1[i], y2[i]))
            y2.append(y2[i] + h * functions2(y1[i], y2[i]))
        # for i in range(num):
        #     y1r.append(fun1r(x[i]))
        #     y2r.append(fun2r(x[i]))
        return x, y1, y2
    else:
        i = 1
        while True:
            x1, y1, y2 = eulerian_first_grade_method(functions1, functions2, beg, end, y10, y20, i * num)
            x2, y21, y22 = eulerian_first_grade_method(functions1, functions2, beg, end, y10, y20, i * 2 * num)
            acc1 = 0
            acc2 = 0
            for j in range(len(x1)):
                acc1 += (y1[j] - y21[2 * j]) ** 2
                acc2 += (y2[j] - y22[2 * j]) ** 2
            # acc1 = sf.square_accuracy(y1, y2)
            # acc2 = sf.square_accuracy(y21, y22)
            # print('acc1 = ', acc1, ' ', 'acc2=', acc2)
            # print(i * 2 * num)
            if acc1 < eps and acc2 < eps:
                # print('acc1 = ', acc1, ' ', 'acc2=', acc2)
                return x2, y21, y22, i * 2 * num
            i *= 2


def eulerian_second_grade(fun1, fun2, beg, end, y10, y20, num, eps=None):
    if eps == None:
        x, y1, y2 = [], [], []
        h = (end - beg) / num
        x.append(beg)
        y1.append(y10)
        y2.append(y20)
        # print(y2[0])
        for i in range(num - 1):
            x.append(x[i] + h)
            k11 = h * fun1(y1[i], y2[i])
            k21 = h * fun2(y1[i], y2[i])
            k12 = h * fun1(y1[i] + k11 / 2, y2[i] + k21 / 2)
            k22 = h * fun2(y1[i] + k11 / 2, y2[i] + k21 / 2)
            y1.append(y1[i] + (k11 + k12) / 2)
            y2.append(y2[i] + (k21 + k22) / 2)
        # print(y1, '\n', y2)
        return x, y1, y2
    else:
        i = 1
        while True:
            x1, y1, y2 = eulerian_second_grade(fun1, fun2, beg, end, y10, y20, i * num)
            x2, y21, y22 = eulerian_second_grade(fun1, fun2, beg, end, y10, y20, i * 2 * num)
            # print(y1)
            # print(y21)
            acc1 = 0
            acc2 = 0
            for j in range(len(x1)):
                acc1 += (y1[j] - y21[2 * j]) ** 2
                acc2 += (y2[j] - y22[2 * j]) ** 2
            # print('acc1 = ', acc1, ' ', 'acc2=', acc2)
            # print(i * 2 * num)
            if acc1 < eps and acc2 < eps:
                # print('acc1 = ', acc1, ' ', 'acc2=', acc2)
                return x2, y21, y22, i * 2 * num
            i *= 2


def eulerian_third_grade(fun1, fun2, beg, end, y10, y20, num, eps=None):
    if eps == None:
        x, y1, y2 = [], [], []
        h = (end - beg) / num
        x.append(beg)
        y1.append(y10)
        y2.append(y20)
        for i in range(num - 1):
            x.append(x[i] + h)
            k11 = h * fun1(y1[i], y2[i])
            k21 = h * fun2(y1[i], y2[i])
            k12 = h * fun1(y1[i] + k11 / 2, y2[i] + k21 / 2)
            k22 = h * fun2(y1[i] + k11 / 2, y2[i] + k21 / 2)
            k13 = h * fun1(y1[i] + k12 / 2, y2[i] + k22 / 2)
            k23 = h * fun2(y1[i] + k12 / 2, y2[i] + k22 / 2)
            y1.append(y1[i] + k11 / 6 + k12 / 2 + k13 / 3)
            y2.append(y2[i] + k21 / 6 + k22 / 2 + k23 / 3)
        # print(y1, '\n', y2)
        return x, y1, y2
    else:
        i = 1
        while True:
            x1, y1, y2 = eulerian_third_grade(fun1, fun2, beg, end, y10, y20, i * num)
            x2, y21, y22 = eulerian_third_grade(fun1, fun2, beg, end, y10, y20, i * 2 * num)
            acc1 = 0
            acc2 = 0

            for j in range(len(y1)):
                acc1 += float((y1[j] - y21[2 * j]) ** 2)
                # print(y1[j], ' ', y21[2*j] )
                acc2 += (y2[j] - y22[2 * j]) ** 2
            # print('acc1 = ', acc1, ' ', 'acc2=', acc2)
            # print(i * 2 * num)
            if acc1 < eps and acc2 < eps:
                # print('acc1 = ', acc1, ' ', 'acc2=', acc2)
                return x2, y21, y22, i * 2 * num
            i *= 2


def eulerian_fourth_grade(fun1, fun2, beg, end, y10, y20, num, eps=None):
    if eps == None:
        x, y1, y2 = [], [], []
        h = (end - beg) / num
        x.append(beg)
        y1.append(y10)
        y2.append(y20)
        for i in range(num - 1):
            x.append(x[i] + h)
            k11 = h * fun1(y1[i], y2[i])
            k21 = h * fun2(y1[i], y2[i])
            k12 = h * fun1(y1[i] + k11 / 2, y2[i] + k21 / 2)
            k22 = h * fun2(y1[i] + k11 / 2, y2[i] + k21 / 2)
            k13 = h * fun1(y1[i] + k12 / 2, y2[i] + k22 / 2)
            k23 = h * fun2(y1[i] + k12 / 2, y2[i] + k22 / 2)
            k14 = h * fun1(y1[i] + k13 / 2, y2[i] + k23 / 2)
            k24 = h * fun2(y1[i] + k13 / 2, y2[i] + k23 / 2)
            y1.append(y1[i] + 1 / 6 * k11 + 1 / 3 * k12 + 1 / 3 * k13 + 1 / 6 * k14)
            y2.append(y2[i] + 1 / 6 * k21 + 1 / 3 * k22 + 1 / 3 * k23 + 1 / 6 * k24)
        return x, y1, y2
    else:
        i = 1
        while True:
            x1, y1, y2 = eulerian_fourth_grade(fun1, fun2, beg, end, y10, y20, i * num)
            x2, y21, y22 = eulerian_fourth_grade(fun1, fun2, beg, end, y10, y20, i * 2 * num)
            acc1 = 0
            acc2 = 0
            for j in range(len(y1)):
                acc1 += (y1[j] - y21[2 * j]) ** 2
                acc2 += (y2[j] - y22[2 * j]) ** 2
            # print('acc1 = ', acc1, ' ', 'acc2=', acc2)
            # print(i * 2 * num)
            if acc1 < eps and acc2 < eps:
                # print('acc1 = ', acc1, ' ', 'acc2=', acc2)
                return x2, y21, y22, i * 2 * num
            i *= 2


def adams_third_grade(f1, f2, beg, end, y11, y12, y13, y21, y22, y23, num, eps=None):
    if eps is None:
        h = (end - beg) / num
        x = [beg, beg + h, beg + 2 * h]
        y1 = [y11, y12, y13]
        y2 = [y21, y22, y23]
        for i in range(num - 3):
            y1.append(y1[i + 2] + h * (f1(x[i + 2], y1[i + 2], y2[i + 2]) * 23 / 12 -
                                       f1(x[i + 1], y1[i + 1], y2[i + 1]) * 4 / 3 +
                                       f1(x[i], y1[i], y2[i]) * 5 / 12))
            y2.append(y2[i + 2] + h * (f2(x[i + 2], y1[i + 2], y2[i + 2]) * 23 / 12 -
                                       f2(x[i + 1], y1[i + 1], y2[i + 1]) * 4 / 3 +
                                       f2(x[i], y1[i], y2[i]) * 5 / 12))
            x.append(x[i + 2] + h)

        return x, y1, y2
    else:
        i = 1
        while True:

            x1, z, t = adams_third_grade(f1, f2, beg, end, y11, y12, y13, y21, y22, y23, i * num)
            x2, e, l = adams_third_grade(f1, f2, beg, end, y11, y12, y13, y21, y22, y23, i * 2 * num)
            acc1 = 0
            acc2 = 0
            # print(len(z), len(e))
            # break
            # #
            for j in range(len(z)):
                acc1 += (z[j] - e[2 * j]) ** 2
                acc2 += (t[j] - l[2 * j]) ** 2
            acc1 /= i * num
            acc2 /= i * num
            # print('acc1 = ', acc1, ' ', 'acc2=', acc2)
            if acc1 < eps and acc2 < eps:
                return x2, e, l, i * 2 * num
            i *= 2


def adams_fourth_grade(f1, f2, beg, end, y11, y12, y13, y14, y21, y22, y23, y24, num, eps=None):
    if eps is None:
        h = (end - beg) / num
        x = [beg, beg + h, beg + 2 * h, beg + 3 * h]
        y1 = [y11, y12, y13, y14]
        y2 = [y21, y22, y23, y24]
        for i in range(num-4):
            y1.append(y1[i + 3] * h * (f1(x[i + 3], y1[i + 3], y2[i + 3]) * 55 / 24 -
                                       f1(x[i + 2], y1[i + 2], y2[i + 2]) * 59 / 24 +
                      f1(x[i + 1], y1[i + 1], y2[i + 1]) * 37 / 24 -
                      f1(x[i], y1[i], y2[i]) * 3 / 8))
            y2.append(y2[i + 3] * h * (f2(x[i + 3], y1[i + 3], y2[i + 3]) * 55 / 24 -
                                       f2(x[i + 2], y1[i + 2], y2[i + 2]) * 59 / 24 +
                      f2(x[i + 1], y1[i + 1], y2[i + 1]) * 37 / 24 -
                      f2(x[i], y1[i], y2[i]) * 3 / 8))
            x.append(x[i + 2] + h)

        return x, y1, y2
    else:
        i = 1
        while True:

            x1, z, t = adams_fourth_grade(f1, f2, beg, end, y11, y12, y13, y14, y21, y22, y23, y24, i * num)
            x2, e, l = adams_fourth_grade(f1, f2, beg, end, y11, y12, y13, y14, y21, y22, y23, y24, i * 2 * num)
            acc1 = 0
            acc2 = 0
            # print(z)
            # print(e)
            # break
            # print(len(z), len(e))
            # break
            # #
            for j in range(len(z)):
                # print(acc1, acc2)
                acc1 += ((z[j] - e[2 * j]) ** 2)
                acc2 += ((t[j] - l[2 * j]) ** 2)
            acc1/=i*num
            acc2/=i*num
            if acc1 < eps and acc2 < eps:
                return x2, e, l, i * 2 * num
            i *= 2
