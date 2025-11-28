# Problem-2: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
 
#   Output: (examples)
#     1) input a = 1, then output : 1
#     2) input a = 2, then output : 1, 3
#     3) input a = 3, then output : 1, 3, 5
#     4) input a = 4, then output : 1, 3, 5, 7


a = int(input("Enter a number: "))
numbers = []
print("Output:", end=" ")

current_number = 1
for i in range(a):
    numbers.append(current_number)
    current_number += 2

print(*numbers, sep=", ")
