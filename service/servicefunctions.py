def epsilon(grade):
    return 10 ** (-grade)


def square_accuracy(y, yt):
    sum = 0
    for i in range(len(y)):
        sum += (y[i] - yt[i]) ** 2
    return sum


def eps_acc(y1, y2):
    sum = 0
    j = 1
    for i in range(len(y1)):
        sum += (y2[2 * j] - y1[j]) ** 2
    return sum
