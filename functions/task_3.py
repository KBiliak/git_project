# Написати функцію get_filtered(), що приймає 1 аргумент - список
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], і виводить на консоль всі
# елементи які менші 5. (for/while + if) (20 балів)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def get_filtered(a):
    for num in a:
        if num < 5:
            print(num)

get_filtered(a)