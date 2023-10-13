# Написати функцію season, що приймає 1 аргумент - номер місяця (від 1 до 12),
# і повертає пору року, якому цей місяць належить (зима, весна, літо чи осінь).

WINTER_MONTHS = (1, 2, 12)
SPRING_MONTHS = (3, 4, 5)
SUMMER_MONTHS = (6, 7, 8)
AUTUMN_MONTHS = (9, 10, 11)

num_of_month = int(input("Enter number of month to get a season: "))
def season(num_of_month):
    if num_of_month in WINTER_MONTHS:
        print("winter")
    elif num_of_month in SPRING_MONTHS:
        print("spring")
    elif num_of_month in SUMMER_MONTHS:
        print("summer")
    elif num_of_month in AUTUMN_MONTHS:
        print("autumn")

season(num_of_month)