# Find the Sum, of all 3 & 5 Multiples Below 1000

# Example: Below 10
# Multiples of 3 = 3,6,9
# Multiples of 10 = 5
# Summation 3 + 5 + 6 + 9 = 23



# Initializing Lists & Variables
mult_3_5 = []
duplicates = []
index = 0

print("\n\n") # Give the Chef space to cook.


# Iterate through each element
for i in (range(1000)):

    # Check if Index Isn't Zero and If Index is a Multiple of 3.
    if i != 0 and i % 3 == 0:
        mult_3_5.append(i)

    # Check if Index Isn't Zero and If Index is a Multiple of 5.
    if i != 0 and i % 5 == 0:
        mult_3_5.append(i) 

# Remove Duplicates Created From Common Multiples of 3 & 5
while index < len((mult_3_5)) - 1:

    if mult_3_5[index] == mult_3_5[index+1]:
        duplicates.append(mult_3_5[index])
        index += 1
    else:
        index += 1



# Prints List Length
print(f"\nList Length: {len(mult_3_5)}")

# Prints List
print(f"\nList of 3 & 5 Multiples: {mult_3_5}")

# Prints Duplicates
print(f"\nDuplicates: {duplicates}")



# Adds All Multiples Together
sum_mult_3_5 = sum(mult_3_5)

# Adds All Duplicates Together
sum_duplicates = sum(duplicates)

# Subtracts Duplicates from Summation.
total = sum_mult_3_5 - sum_duplicates


# Prints Answer!
print(f"\n\nFinal Answer: {total}")



