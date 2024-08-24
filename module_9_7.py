def is_prime(func):
    def wrapper(x, y, z):
        result = func(x, y, z)
        if result > 1:
            for i in range(2, result - 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        return result
    return wrapper

@is_prime
def sum_three(x, y, z):
    return x + y + z


result = sum_three(2, 3, 6)
print(result)