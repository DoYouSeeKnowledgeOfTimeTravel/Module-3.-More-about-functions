data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_structure_sum(*args):
    for number in data_structure[0]:
        str_number = str(number)
        print(*str_number)



    # numbers = data_structure[0]
    # total = 0
    # for number in numbers:
    #     total += number
    # print(total)


calculate_structure_sum(data_structure)
# print(result)
