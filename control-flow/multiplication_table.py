number =  input("Enter a number you want to see its multiplication table: ")
number = int(number)
for i in range(1, 13):
    result = number * i
    print(f"{number} x {i} = {result}") 
    