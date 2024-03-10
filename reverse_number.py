def reverse(n):
    x = []
    # reverse = 0
    while n != 0:
        remainder = n % 10
        # reverse = (reverse * 10) + remainder
        x.append(remainder)
        n = n//10

    return x
    # return reverse

print(reverse(85641))