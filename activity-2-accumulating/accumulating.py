def total_of(numbers):
    total = 0
    for number in numbers:
        if number > 10:
            total = total + number
    return total


# def largest_of(numbers):
#     biggest = numbers[0]
#     for number in numbers:
#         if number > biggest:
#             biggest = number
#     return biggest

def smallest_of(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest

readings = [12, 7, 19, 3]

print(total_of(readings))
print(total_of([]))
print(smallest_of(readings))
