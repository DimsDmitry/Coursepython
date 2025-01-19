# Создайте функцию get_coordinates, которая возвращает кортеж с двумя значениями: широтой и долготой.
# Затем распакуйте этот кортеж в две переменные и выведите их.

def get_coordinates():
    return (40.7128, -74.0060)


latitude, longitude = get_coordinates()
print(latitude, longitude)
