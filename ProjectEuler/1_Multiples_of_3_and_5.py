# Problem 1 - Multiples of 3 & 5

# Find the Sum, of all 3 & 5 Multiples Below 1000

# Example: Below 10
# Multiples of 3 = 3,6,9
# Multiples of 10 = 5
# Summation 3 + 5 + 6 + 9 = 23




mult_3_5 = []

duplicates = []

index = 0


print("\n\n") # Give the Chef space to cook.


for i in (range(1000)):

    if i != 0 and i % 3 == 0:

        mult_3_5.append(i)

    if i != 0 and i % 5 == 0:

        mult_3_5.append(i) 


# Remove Duplicates Created From Common Multiples
while index < len((mult_3_5)) - 1: 

    if mult_3_5[index] == mult_3_5[index+1]:

        duplicates.append(mult_3_5[index])

        index += 1

    else:

        index += 1


sum_mult_3_5 = sum(mult_3_5)

sum_duplicates = sum(duplicates)

total = sum_mult_3_5 - sum_duplicates


print(f"\nList Length: {len(mult_3_5)}")

print(f"\n3 & 5 Multiples: {mult_3_5}")

print(f"\nDuplicates: {duplicates}")

print(f"\n\nFinal Answer: {total}")



