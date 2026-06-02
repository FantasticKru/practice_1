grades = [90, 80, 70, 60, 50]
passed = 0

for grade in grades:
    if grade >= 70:
        passed += 1
print("Number of passing grades:", passed)