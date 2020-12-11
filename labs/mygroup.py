def print_students(students):
    print(u"Имя".ljust(10), u"Фамилия".ljust(10),
          u"Экзамены".ljust(50), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(10),
              student["surname"].ljust(10), str(student["exams"]).ljust(50),
              str(student["marks"]).ljust(20))


def filter(groupmates, sb):
    id = 0
    idd = []
    for groupmate in groupmates:
        id =int( id + 1)
        ss = 0

        for mark in groupmate["marks"]:
            ss = ss + mark
        ss = ss / 3

        if ss >= sb:
            idd.append(id)
    return idd


groupmates = [
    {
        "name": "Александр",
        "surname": "Фесенко",
        "exams": ["Информатика", "Операционные системы", "Web"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Алексей",
        "surname": "Зебрин",
        "exams": ["Стандартизация", "АиГ", "КТП"],
        "marks": [5, 4, 3]
    },
    {
        "name": "Михей",
        "surname": "Котков",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [4, 3, 4]
    }
]

print_students(groupmates)
print('')
sb = int(input('Введите средний балл - '))
print('')

ids = filter(groupmates, sb)

filter = []

for elem in ids:
    filter.append(groupmates[elem])

print_students(filter)
