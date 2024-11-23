# Задание "Средний балл"
# Создаём cписок оценок (grades) для каждого ученика в алфавитном порядке.
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(grades)
# Создаём множество (students), которое содержит неупорядоченную последовательность имён
# всех учеников в классе.
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(students)
# Сортируем имена учеников по алфавиту
sorted_students = sorted(students)
print(sorted(students))
# Создаём пустой словарь для хранения средних баллов
average_grades = {}
# Рассчитываем средний балл для каждого ученика, заполняем словарь и выводим результат.
for i, student in enumerate(sorted_students):
    average_grades[student] = sum(grades[i]) / len(grades[i])
print(average_grades)
