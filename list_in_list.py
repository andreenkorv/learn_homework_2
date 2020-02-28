# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
# ???
print("Задание №1 \n")
my_dict = {
  element['first_name']: students.count(element) for element in students
  }
for key in my_dict:
    print(f'{key}: {my_dict[key]}')
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
# ???
print("\nЗадание №2 \n")
my_dict = {
  element['first_name']: students.count(element) for element in students
  }
max_col = 0
for key in my_dict:
    if my_dict[key] >= max_col:
        max_col = my_dict[key]
        name = key
print(f'Самое частое имя среди учеников: {name}')
# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
print("\nЗадание №3 \n")
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ],
  [
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
    {'first_name': 'Оля'},
    {'first_name': 'Оля'},
    {'first_name': 'Оля'}
  ]
]
# ???
class_list = []
# print(school_students[0], len(school_students))
for i in range(len(school_students)):
    my_dict = {
        element['first_name']: school_students[i].count(element) for element in students
            }
    max_col = 0
    class_number = i
    for key in my_dict:
        if my_dict[key] >= max_col:
            max_col = my_dict[key]
            name = key
    print(f'Самое частое имя в классе {class_number+1}: {name}')
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
print("\nЗадание №4 \n")
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
  {'class': '4c', 'students': [{'first_name': 'Евгений'}, {'first_name': 'Жора'}, {'first_name': 'Маргарита'}, {'first_name': 'Есения'}]}
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
  'Жора': True,
  'Маргарита': False,
  'Есения': False,
  'Евгений': True
}
# ???
for element in school:
    boys = 0
    for item in element['students']:
        # print(item['first_name'])
        if is_male[item['first_name']]:
            boys += 1
    girls = len(element['students']) - boys
    print(f'В классе {element["class"]} {girls} девочки {boys} мальчика.')
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
print("\nЗадание №5 \n")
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
  {'class': '4c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Жора'}]},
  {'class': '5c', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}, {'first_name': 'Есения'}]}

]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
  'Жора': True,
  'Маргарита': False,
  'Есения': False,
  'Евгений': True
}
# ???
max_boys = 0
max_girls = 0
for element in school:
    boys = 0
    for item in element['students']:
        # print(item['first_name'])
        if is_male[item['first_name']]:
            boys += 1
    girls = len(element['students']) - boys
    if max_boys < boys:
        max_boys = boys
        class_boys_name = element["class"]
    if max_girls < girls:
        max_girls = girls
        class_girsl_name = element["class"]

print(f'Больше всего мальчиков в классе {class_boys_name}')
print(f'Больше всего девочек в классе {class_girsl_name}')
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a