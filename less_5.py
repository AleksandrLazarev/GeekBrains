# task_1
def odd_nums (n):
    for n in range(1, n + 1, 2):
        yield n
for i in odd_nums(15):
    print(i)

# task_3

from itertools import islice, zip_longest

tutors = ["Иван", "Анастасия", "Пётр", "Сергей", "Дмитрий", "Борис", "Елена",
          "Кирилл"]
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

rezult = (i for i in zip_longest(tutors, klasses))

print(type(rezult))
print(*islice(rezult, 9))
print(list(islice(rezult, 3)))

# task_4

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# print([i for i in src if src.count(i) == 1])
result = [src[num] for num in range(1, len(src)) if src[num] > src[num - 1]]
print(result)