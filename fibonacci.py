def fibo(n):
    a = 0
    b = 1

    x = [0, 1]
    for i in range(n):
        c = a + b

        x.append(c)

        a, b = b, c

    return x

print(fibo(10))