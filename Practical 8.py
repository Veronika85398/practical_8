# Функция как тип
# Задание 1
# Создайте функцию say_hi, сохраните её в переменную other и вызовите через
# other.
def say_hi():
    print("Привет!")

other = say_hi
other()
# Задание 2
# Создайте функцию cube(x), два имени для неё и выведите результаты для 2 и 3.
def cube(x):
    return x ** 3

f1 = cube
f2 = cube

print(f1(2))  # 8
print(f2(3))  # 27
# Задание 3
# Сравните тип функции get_five и тип результата её вызова get_five() с помощью
# type(). Выведите оба типа.
def get_five():
    return 5

print(type(get_five))    # <class 'function'>
print(type(get_five()))  # <class 'int'>
# Функция как параметр функции
# Задание 4
# Напишите функцию run(action), которая вызывает переданную функцию
# приветствия.
def hello():
    print("Здравствуйте!")

def run(action):
    action()

run(hello)  # Здравствуйте!
# Задание 5
# Напишите apply(action, number), передайте ей функцию удвоения и число 6.
def double(x):
    return x * 2

def apply(action, number):
    return action(number)

print(apply(double, 6))  # 12
# Задание 6
# Напишите transform(values, action), которая возвращает список результатов
# применения функции прибавления 10 к числам [1, 2, 3].
def add_ten(x):
    return x + 10

def transform(values, action):
    return [action(v) for v in values]

print(transform([1, 2, 3], add_ten))  # [11, 12, 13]
# Функция как результат функции
# Задание 7
# Напишите factory(), возвращающую функцию, которая выводит текст «Работает».
# Вызовите возвращённую функцию.
def factory():
    def inner():
        print("Работает")
    return inner

result = factory()
result()  # Работает
# Задание 8
# Напишите make_adder(value), возвращающую функцию прибавления value к
# переданному числу. Проверьте на числах 5 и 7.
def make_adder(value):
    def adder(x):
        return x + value
    return adder

add5 = make_adder(5)
add7 = make_adder(7)

print(add5(10))  # 15
print(add7(10))  # 17
# Задание 9
# Напишите make_counter(), возвращающую функцию-счётчик. Каждый её вызов
# должен возвращать следующее число, начиная с 1.
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c = make_counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3