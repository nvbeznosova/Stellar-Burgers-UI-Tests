def digit_root(num):
    while num > 9:
        digits = [int(d) for d in str(num)]
        num = sum(digits)
    return num
