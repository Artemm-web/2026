'''
Лабораторна №2
'''

users = {
    "student1": {
        "password": "1234",
        "grades": [10, 8, 12, 7, 4, 9]
    },
    "student2": {
        "password": "qwerty",
        "grades": [5, 6, 3, 11, 9, 2]
    },
    "student3": {
        "password": "asd123",
        "grades": [12, 10, 8, 4, 7, 6]
    },
    "student4": {
        "password": "1256",
        "grades": [3, 4, 5, 7, 9, 12]
    }
}

login = input("Введіть логін: ")
password = input("Введіть пароль: ")

if login in users and users[login]["password"] == password:
    grades = users[login]["grades"]

    print("\nВхід виконано")
    print("Ваші оцінки:", grades)

    satisfactory = 0
    unsatisfactory = 0

    for grade in grades:
        if 5 <= grade <= 12:
            satisfactory += 1
        elif 1 <= grade <= 4:
            unsatisfactory += 1

    print("Кількість задовільних оцінок (5-12):", satisfactory)
    print("Кількість незадовільних оцінок (1-4):", unsatisfactory)

else:
    print("\nНеправильний логін або пароль!")