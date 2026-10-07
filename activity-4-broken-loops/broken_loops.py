# Three of the things below are wrong. Nothing crashes, and nothing hangs.


def count_to(n):
    for i in range(1, n + 1):
        print(i)


def total_of(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total


def delivery_outcome(door_log):
    attempts = 0
    for knock in door_log:
        attempts = attempts + 1
        if knock == "answered":
            return f"Delivered on attempt {attempts}"
        if attempts >= 3:
            return "Returned to depot"
        print (attempts)
    return "Ran out of days"


count_to(5)
print(total_of([12, 7, 19, 3]))
print(delivery_outcome(["no answer", "no answer", "no answer","no answer","no answer"]))
