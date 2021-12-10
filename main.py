print('Лестница')

# Пользователь вводит число N.
# Программа выводит “лесенку” из чисел:

# Пример:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

number = int(input('Введите число: '))

for i in range(1, number + 1):
  string = []
  for j in range(i):
    string.append(i)
  print(' '.join(map(str, string)))
