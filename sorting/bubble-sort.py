print()
print("Bubble sort")
print("oOoOoOoOoOo", end='\n\n')

numbers = [4, 9, 7, 1, 3, 6, 2, 10, 8, 5]
num_len = len(numbers)

swapped = True
while swapped is True:
    swapped = False
    for i in range(0, num_len - 1):
        if numbers[i] > numbers[i+1]:
            temp = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = temp
            swapped = True

# output
for i in range(0, num_len):
    print(numbers[i])