"""
Задача №1.
Есть у нас список учеников которые сдавали тест
Нужно вывести средний балл всех стужентов ,
этот результат надо сравнить со своим баллом
Если ваш балл ниже среднего значит надо вернуть "Провал"
Если ваше балл выше надо вернуть "Прошел"
"""

class_point = [12, 43, 86, 97, 76]
my_point = 63


def average(class_point, my_point):
    print(sum(class_point) / len(class_point))
    return "Passed" if (sum(class_point) / len(class_point)) < my_point else "Fail"
    # if (sum(class_point) / len(class_point)) < my_point:
    #     return "Passed"
    # return "Fail"


# print(average(class_point, my_point))


# def arenda(days):
#     return (days * 40) if days <= 3 else (days * 40) - 20 if 3 < days < 7 else (days * 40) - 50
#
#
# print(arenda(3))
