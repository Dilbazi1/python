def int_func(var):
    return var.title()


print(int_func('sdjdj'))
user_string = input("введите строку ")
user_words = user_string.split()
for i in user_words:
    print(int_func(i))

#print(user_words)
