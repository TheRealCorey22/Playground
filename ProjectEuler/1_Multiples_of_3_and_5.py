# Find All Multiples of 3 & 5 Below 1000
# Find the Sum of all Multiples

# Example: 3,5,6,9 = 23 -- Is the Summation of all 3 & 5 Multiples Below 10.

mult_3 = []

mult_5 = []

for i in (range(1000)):
    print(i)
    
    if i != 0 and i % 3 == 0:
        mult_3.append(i)

    if i != 0 and i % 5 == 0:
        mult_5.append(i)


print(mult_3)

print("\n\n")

print(mult_5)