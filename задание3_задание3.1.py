def division(var1, var2):
    try:
        return var1 / var2
    except ZeroDivisionError:
        return


var1 = int(input("введите первое число"))
var2 = int(input("введите втарое число"))
print(division(var1, var2))
