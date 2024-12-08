def test_func():
    pass #Ничего не произойдет 


test_func()


def test_func_1():
    print('Hello', end = '')  #Встроенная функция
    print('!')

test_func_1()


def test_func_2(name):
    print(f"hello, {name}")


test_func_2('Dima')
test_func_2(3)
test_func_2(7.7)


def test_func_3(a, b):
    c = a + b
    print(f"Result: {c}")


test_func_3(1.7, 6)
test_func_3('He', 'll')

# Or

def summa(a, b):
    return a + b   #Указывает что будет возвращаться из функции

c = summa(3,4.7)
print(c)
print(summa("Ri", 'p'))


def minimal(l):   #Нахождение наименьшего чичсла из списка
    min = l[0]   
    for i in l:
        if i < min:
            min = i
    print(min)


num1 = [5, 6, 7, 3]
minimal(num1)

num2 = [1.6, 4.7, 3.2] 
minimal(num2)


fun = lambda x, y: x ** y
print(fun(2, 5))