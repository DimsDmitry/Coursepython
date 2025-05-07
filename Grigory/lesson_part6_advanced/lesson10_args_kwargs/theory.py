def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

result = multiply(2, 3, 4, 5)
print(result)


def create_user(*args, **kwargs):
    print(kwargs)

create_user(123, username='Олежка1200', age=10, password='1234', male='М')
