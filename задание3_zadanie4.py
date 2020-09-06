def my_func(var1, var2):
    var3 = abs(var2)
    i = 1
    s = 1
    for i in range(var3):
        s = s * var1

    return 1 / s


def my_func1(var1, var2):
    return var1 ** var2


var1 = float(input("введите действительное положительное число"))
var2 = int(input('введите целое отрицательное число'))

print(my_func(var1, var2))
print(my_func1(var1, var2))
