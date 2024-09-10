#Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#Пустые списки для простых и составных чисел
primes = []
not_primes = []

#Проверка чисел
for num in numbers:
    if num < 2:  #Если число меньше 2,оно не простое
        not_primes.append(num)
    else:
        is_prime = True  # Предполагаем, что число простое
        for i in range(2, int(num ** 0.5) + 1):  # Проверка на делители
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        else:
            not_primes.append(num)

#Вывод списков
print("Primes:", primes)
print("Not Primes:", not_primes)