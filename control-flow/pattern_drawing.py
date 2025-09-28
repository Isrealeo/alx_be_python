pattern_size = input("Enter size of the pattern): ")
pattern_size = int(pattern_size)
while pattern_size >= 0:
    for i in range(pattern_size):
        print("*" * (i + 1))
    pattern_size -= 1
