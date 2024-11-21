immutable_var = 1, 2.3, 'hi'
print(immutable_var)
#из-за свойства неизменяемости у объекта типа кортеж, следующая строка не исполняется(есть исключение: в кортеже, внутри списка, значения менять можно)
immutable_var[0] = 5
mutable_list = [1, 2.3, 4, 'l']
mutable_list[0] = 3
print(mutable_list)