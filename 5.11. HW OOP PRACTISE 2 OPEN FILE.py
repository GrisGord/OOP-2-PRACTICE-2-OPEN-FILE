import pprint
                            # ЗАДАНИЕ №1.

    # Открываем текстовый файл для чтения
with open(r'D:\IT\NETOLOGY\OOP\PRACTICE 2\recipes.txt', encoding='utf-8') as f:
    cook_book = {}
    # Пока не достигнут конец файла
    while True:
        # Читаем первую строку, это название блюда
        dish_name = f.readline().strip()
        # Если достигнут конец файла, выходим из цикла
        if not dish_name:
            break
        # Читаем вторую строку c количеством ингредиентов
        ingredient_count = int(f.readline().strip())
        # Создаем пустой список для ингредиентов текущего блюда
        ingredients = []
        # Добавляем ингредиенты в список
        for i in range(ingredient_count):
            line = f.readline().strip().split(' | ')
            ingredient_name = line[0]
            quantity = int(line[1])
            measure = line[2]
            ingredient = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
            ingredients.append(ingredient)
        f.readline().strip()
        # Добавляем блюдо с его ингредиентами в словарь cook_book
        cook_book[dish_name] = ingredients

# Выводим полученный словарь cook_book
for k, v in cook_book.items():
    print(f'{k}: \n{pprint.pformat(v)}\n')


                            # ЗАДАНИЕ №2.

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']
            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
    return shop_list

a = get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 1)
pprint.pprint(a)


                            # ЗАДАНИЕ №3

with open(r'D:\IT\NETOLOGY\OOP\PRACTICE 2\1.txt', encoding='utf-8') as f1,\
        open(r'D:\IT\NETOLOGY\OOP\PRACTICE 2\2.txt', encoding='utf-8') as f2,\
        open(r'D:\IT\NETOLOGY\OOP\PRACTICE 2\3.txt', encoding='utf-8') as f3:
    list_f1, list_f2, list_f3 = [], [], []
    dict_f1, dict_f2, dict_f3= {}, {}, {}
    for idx1, line1 in enumerate(f1):
        list_f1.append(line1.strip())
        # print(idx1, line1.strip())
    for idx2, line2 in enumerate(f2):
        list_f2.append(line2.strip())
        # print(idx2, line2.strip())
    for idx3, line3 in enumerate(f3):
        list_f3.append(line3.strip())
        # print(idx3, line3.strip())
    dict_f1[len(list_f1)] = list_f1
    dict_f2[len(list_f2)] = list_f2
    dict_f3[len(list_f3)] = list_f3
    final_dict = dict(list(dict_f1.items()) + list(dict_f2.items()) + list(dict_f3.items()))
    final_dict_sorted = dict(sorted(final_dict.items(), key=lambda item: item[0]))
    # print(final_dict_sorted)

with open(r'D:\IT\NETOLOGY\OOP\PRACTICE 2\final_file.txt','w', encoding='utf-8') as ff:
    data = ff.write(f'2.txt\n{len(list_f2)}\n{'\n'.join(final_dict_sorted[len(list_f2)])}\n'
                    f'1.txt\n{len(list_f1)}\n{'\n'.join(final_dict_sorted[len(list_f1)])}\n'
                    f'3.txt\n{len(list_f3)}\n{'\n'.join(final_dict_sorted[len(list_f3)])}'
                    )
with open(r'D:\IT\NETOLOGY\OOP\PRACTICE 2\final_file.txt', encoding='utf-8') as ff:
    data = ff.read()
    print(data)
