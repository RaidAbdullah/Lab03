#Program 2
list1 = []

for i in range(10):
  value = float(input(f"Enter value {i + 1}: "))
  list1.append(value)

largest = list1[0]
for i in range(1, len(list1)):
    if list1[i] > largest:
        largest = list1[i]

# Display the largest number
print(f"The largest number in the list is {largest}")

