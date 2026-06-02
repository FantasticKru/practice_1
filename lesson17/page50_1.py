numbers = []
for x in range(4):
    numbers.append(int(input("Enter a number: ")))

for n in numbers:
    if n < 0:
        print(n)