def recursive_sum(number: int):
    if number <= 1:
        return number
    return recursive_sum(number - 1) + number
result = recursive_sum(3)
print(result)

print(recursive_sum(5))
print(recursive_sum(10))