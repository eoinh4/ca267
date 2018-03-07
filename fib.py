def fib(num):
    list = []
    j = 1
    i = 0
    last = 1
    while i < num:
        list.append(j)
        last, j = j, last + j
        i = i + 1
    return list
