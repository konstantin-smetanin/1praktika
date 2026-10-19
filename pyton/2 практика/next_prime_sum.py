def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def min_to_prime(numbers):
    total_sum = sum(numbers)
    addition = 0
    while not is_prime(total_sum + addition):
        addition += 1   
    return addition
print(min_to_prime([3, 1, 2]))         # Выведет: 1  (сумма 6 -> 7)
print(min_to_prime([2, 12, 8, 4, 6]))  # Выведет: 5  (сумма 32 -> 37)
print(min_to_prime([5, 2]))            # Выведет: 0  (сумма 7 уже простая)
