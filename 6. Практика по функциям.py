def find_max(list_):
    max = list_[0]
    for i in list_:
        if i > max:
            max = i
    return max

# print(find_max([12.43, 853, 9531, 9, 32]))

# Подсчет четных чисел в списке
def calcu_even(list_):
    counter = 0
    for i in list_:
        if i == 0:
            continue
        if i % 2 == 0:
            counter += 1
    return counter

# print(calcu_even([123, 28, 530, 81, 90, 120]))

def unique(list_):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(unique([123, 28, 530, 81, 90, 120, 29, 29, 123]))