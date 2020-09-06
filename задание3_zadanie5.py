z = 0
while 1:
    i = input("введите числа")
    i = i.split(" ")
    a = 0
    while a < len(i):
        try:
            i[a] = int(i[a])
            z = z + i[a]
        except ValueError:
            print("Value Error")
            print(z)
            break

        a = a + 1

    for c in i:
        z = z + c
    print(z)


