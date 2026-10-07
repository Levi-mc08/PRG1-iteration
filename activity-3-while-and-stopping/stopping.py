# def countdown(start):
#     count = start
#     while count > 0:
#         print(count)
#         count = count - 1
#     print("Liftoff")

def countdown(start):
    count = start
    for count in range(count, 0, -1):
        print(count)
    print("Liftoff")


def first_over(limit, readings):
    readcount = 0
    for reading in readings:
        readcount += 1
        if reading > limit:
            return readcount
    return None


countdown(3)
countdown(0)

print(first_over(100, [45, 92, 130, 88]))
print(first_over(100, [45, 92, 88]))
