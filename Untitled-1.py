# ЗАДАНИЕ 1№
def convert_temperature(celsius: float) -> float:
    """Переводит градусы Цельсия в градусы Фаренгейта."""
    return celsius * 9 / 5 + 32
print(convert_temperature(5))

# ЗАДАНИЕ 2№
def factorial(n: int) -> int:
    """Вычисляет факториал целого числа n."""
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")       
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))