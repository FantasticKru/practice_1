number = input("Enter a positive number: ")
if int(number) > 0:
    n = 1
    while n <= int(number):
        print(n)
        n += 1
else:
    print("The number is not positive.")