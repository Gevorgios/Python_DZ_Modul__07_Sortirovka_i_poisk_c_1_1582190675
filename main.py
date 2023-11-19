# def sort_list(lst):
#     if sum(lst) / len(lst) > 0:
#         sorted_lst = sorted(lst[:int(len(lst) * 2 / 3)])
#     else:
#         sorted_lst = lst[:int(len(lst) / 3)]
#     reversed_lst = lst[int(len(lst) * 2 / 3):][::-1]
#     return sorted_lst + reversed_lst
# my_list = [3, 1, -2, 4, 0, 5, -1, 2]
# sorted_list = sort_list(my_list)
# print(sorted_list)


# def display_grades(grades):
#     print("Оценки студента:", grades)
#
# def retake_exam(grades):
#     index = int(input("Введите номер оценки для пересдачи (от 1 до 10): "))
#     new_grade = int(input("Введите новую оценку (от 1 до 12): "))
#     grades[index - 1] = new_grade
#     print("Оценка успешно изменена.")
#
# def check_scholarship(grades):
#     average_grade = sum(grades) / len(grades)
#     if average_grade >= 10.7:
#         print("Студент имеет право на стипендию.")
#     else:
#         print("Студент не имеет права на стипендию.")
#
# def sort_grades(grades):
#     sort_order = input("Выберите порядок сортировки (возрастание/убывание): ").lower()
#     if sort_order == "возрастание":
#         sorted_grades = sorted(grades)
#     elif sort_order == "убывание":
#         sorted_grades = sorted(grades, reverse=True)
#     else:
#         print("Неверный выбор сортировки.")
#         return
#     print("Отсортированные оценки:", sorted_grades)
#
#
# def main():
#     grades = []
#     for i in range(10):
#         grade = int(input("Введите оценку (от 1 до 12): "))
#         grades.append(grade)
#
#     while True:
#         print("\nМеню:")
#         print("1. Вывод оценок")
#         print("2. Пересдача экзамена")
#         print("3. Проверка стипендии")
#         print("4. Вывод отсортированного списка оценок")
#         print("5. Выход")
#
#         choice = int(input("Выберите пункт меню (от 1 до 5): "))
#
#         if choice == 1:
#             display_grades(grades)
#         elif choice == 2:
#             retake_exam(grades)
#         elif choice == 3:
#             check_scholarship(grades)
#         elif choice == 4:
#             sort_grades(grades)
#         elif choice == 5:
#             print("Программа завершена.")
#             break
#         else:
#             print("Неверный выбор меню.")
#
# if __name__ == "__main__":
#     main()

# def bubble_sort(arr):
#     n = len(arr)
#     is_sorted = False
#     while not is_sorted:
#         is_sorted = True
#         for i in range(1, n):
#             if arr[i-1] > arr[i]:
#                 arr[i-1], arr[i] = arr[i], arr[i-1]
#                 is_sorted = False
#         n -= 1
#
# def improved_bubble_sort(arr):
#     n = len(arr)
#     is_sorted = False
#     while not is_sorted:
#         is_sorted = True
#         swaps = 0
#         for i in range(1, n):
#             if arr[i-1] > arr[i]:
#                 arr[i-1], arr[i] = arr[i], arr[i-1]
#                 is_sorted = False
#                 swaps += 1
#         n -= 1
#         if swaps == 0:
#             break
#
#
# numbers = [5, 2, 8, 12, 1, 7, 3]
# print("Исходный список:", numbers)
#
# bubble_sort(numbers)
# print("Отсортированный список (обычная сортировка пузырьком):", numbers)
#
# numbers = [5, 2, 8, 12, 1, 7, 3]
# improved_bubble_sort(numbers)
# print("Отсортированный список (усовершенствованная сортировка пузырьком):", numbers)