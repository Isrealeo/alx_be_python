int(input("Enter size of the pattern): "))
while input >= 0:
    for i in range(pattern_size):
        print("*" * (i + 1))
    pattern_size -= 1
