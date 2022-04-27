import copy
from collections import Counter
# https://github.com/netology-code/py-homeworks-basic/tree/master/7.files
cook_book = {}
static = ['ingredient_name', 'quantity', 'measure']


def is_closed(file_):
    if file_.closed:
        print('Файл закрыт')
    else:
        print('Файл открыт')


with open('recepts.txt', encoding='utf8') as file:
    while True:
        dict_ingredients = []
        key = file.readline().rstrip()
        count_ingredients = int(file.readline())
        for line in range(count_ingredients):
            lines = file.readline().rstrip().split(sep=' | ')
            line_dict = dict(zip(static, lines))
            dict_ingredients.append(line_dict)
        cook_book[key] = dict_ingredients
        if not file.readline():
            print("Конец файла")
            break
        else:
            print("Чтение файла")


def open_cook_book():
    for key, value in cook_book.items():
        print(f'{key}:')
        for ingredients in value:
            print(ingredients)
            # for key_ingr, value_ingr in ingreditnts.items():
            #   print(f'{key_ingr}: {value_ingr}'.strip())

def get_shop_list_by_dishes(dishes, person_count):
    dict_ingredients = {}
    count = Counter(dishes)
    for dish in dishes:
        work_dict = copy.deepcopy(cook_book)
        if dish in cook_book.keys():
            print('Есть в кулинарной книге. Добавил ингридиенты.')
            for ingredient in work_dict[dish]:
              persons = int(ingredient['quantity']) * person_count * count[dish]
              ingredient.update({'quantity': persons})
              key = ingredient.pop('ingredient_name')
              dict_ingredients[key] = ingredient
        else:
            print('Такого блюда нет в кулинарной книге!')
    for key, value in dict_ingredients.items():
        print(key, '-->', value)

print('---------------------')
open_cook_book()
print('---------------------')
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print('---------------------')
get_shop_list_by_dishes(['Омлет','Омлет','Запеченный картофель', 'Омлт', 'Фахитос'], 1)