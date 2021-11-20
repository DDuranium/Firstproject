print("Dinesh is cool")

numbers = [11, 2, 3, 6, 7, 8]


def sum(array_of_numbers):
    sum = 0
    for num in range(len(array_of_numbers)):
       sum += array_of_numbers[num]
    return sum

print(sum(numbers))
