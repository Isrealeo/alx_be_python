Size = int(input("Enter the size of the pattern): "))
while Size > 0:
    for i in range(Size):
        print("*" * (i + 1))
    Size -= 1
