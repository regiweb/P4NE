L = [34, 23, "test1", "test3"]
# выборка из списка с начала до конца через один элемент
L[::2]
print(L)
# добавляем в конец списка элемент
L.append("newitem")
# вставить элемент в определённое место списка
L.insert(3, 555)
print(L)
# удалить элемент по порядку из списка
del L[3]
# удалить элемент по значению
L.remove("test1")
L.remove("test3")
L.remove("newitem")
# удалить дубликаты из списка
L = list(set(L))
for i in L:
    print(i)
# объявление функции
def megafunc (x):
    return x**3+2*x**2+1
a = 5
b = megafunc(a)
print(b)

