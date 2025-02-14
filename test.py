def do_something(a, b):
    return a * b, a + b


# распаковка кортежа:
digit, summ = do_something(2, 10)
print(digit)
print(summ)
