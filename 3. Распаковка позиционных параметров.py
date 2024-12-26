# Распаковка
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(a = 'dsa', b = 5231, c = [95431])
print_params(a = [213, 54], b = None)
print_params()

# Распаковка параметров

values_list = [23, True, [9432, 532]]
values_dict = {'a': 9532, 'b': {6, 93, 19}, 'c': 8412.123}

print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры
values_list_2 = [{True, 94.45}, 123]
print_params(*values_list_2, 42)