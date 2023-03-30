import random

n = 1000
even_count = 0

for i in range(n):
    x = random.randint(1, 1000)
    if x % 2 == 0:
        even_count += 1
percent = even_count / n * 100

print("Процент четных чисел: {:.2f}%".format(percent))
