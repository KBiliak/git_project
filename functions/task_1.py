# Напишіть функцію sum_range(start, end), яка підсумовує всі цілі числа від
# значення start до величини end включно. Якщо користувач задасть перше число
# більше, ніж друге, просто поміняйте їх місцями. (35 балів)
start = int(input("Enter your start number: "))
end = int(input("Enter your end number: "))


def sum_range(start, end):
    if start > end:
        temp = start
        start = end
        end = temp

    res = 0
    for num in range(start, end + 1):
        res += num
    return res

print(sum_range(start, end))