Size = int(input("Enter the size of the pattern: "))
while Size > 0:
    for i in range(Size):
        for j in range(i + 1):
            print("*", end="")
        print()  # move to the next line
    Size -= 1
