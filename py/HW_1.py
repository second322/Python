# 1) Создать переменную типа String
a = 'Hello'

# 2) Создать переменную типа Integer
b = 3

# 3) Создать переменную типа Float
c = 3.2

# 4) Создать переменную типа Bytes
d = bytes(1)

# 5) Создать переменную типа List
e = [10]

# 6) Создать переменную типа Tuple
f = tuple('1', )

# 7) Создать переменную типа Set
g = set(a)

# 8) Создать переменную типа Frozen set
h = frozenset(a)

# 9) Создать переменную типа Dict
i = {'a': 'A'}


# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
print(h, type(h))
print(i, type(i))

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
Str1 = 'Hello '
Str2 = 'World'
Str_Sum = Str1 + Str2
print(Str_Sum)

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(a, b)

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(a + ' ' + str(b))
