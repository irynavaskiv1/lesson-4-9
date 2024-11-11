'''
Скрипт файлу hw_9_2_rand_norm.py реалізує формування нормального закону розподілу випадкової величини,
як адитивна суміш двох рівномірних законів за принципами циклічних повторень.

'''


import numpy as np
from math import sqrt, cos, log
import matplotlib.pyplot as plt

# задаємо параметри вибріки
n = 10000                          #кількість елементів
V1 = np.random.rand(n)             #генерація рівномірних ВВ
V2 = np.random.rand(n)

print(f'Перший рівномірний розподіл: {V1[:20]}\nДругий рівномірний розподіл: {V2[:20]}')
#візуалізуємо ВВ
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].hist(V1, bins=20)
axes[1].hist(V2, bins=20)
plt.show()

# розраховуємо модель закону розподілу
c = 2 * np.pi
R1 = np.zeros(n)
F1 = np.zeros(n)

#с творюємо масиви R1 та F1, де R1 = sqrt(-2*ln(V1)) та F1 = c * V2
for i in range(len(R1)):
    R1[i] = sqrt(-2*log(V1[i]))
    F1[i] = c*V2[i]

# генеруємо нормальний розподіл за формулою norm = R1*cos(F1)
normDest = np.zeros(n)
for i in range(len(normDest)):
    normDest[i] = R1[i] * cos(F1[i])

# будуємо гістограму
plt.hist(normDest, bins=15)
plt.show()
print('Нормальний розподіл: ', normDest)