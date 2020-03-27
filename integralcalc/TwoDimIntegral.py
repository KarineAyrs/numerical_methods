def two_dim_integral(function, begX, endX, begY, endY, num):
    h = (endX - begX) / num
    h1 = (endY - begY) / num
    sum = 0
    for i in range(num - 1):
        for j in range(num - 1):
            x = begX + h / 2 + h * (i + 1)
            y = begY + h1 / 2 + h1 * (j + 1)
            if y >= x ** 2:
                sum += function(x, y) * h1 * h

    return sum
