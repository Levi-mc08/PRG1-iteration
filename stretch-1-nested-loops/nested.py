for row in range(1, 6):
    for column in range(1, 6):
        print(f"{row} x {column} = {row * column}")
    print()


total_printed = 0
for row in range(1, 6):
    for column in range(1, 6):
        total_printed = total_printed + 1
print(total_printed)
