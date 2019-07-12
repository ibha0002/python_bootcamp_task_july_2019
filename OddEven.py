# Program that determines pairs of numbers whose sum is odd and product is even
# In this code I haven't used functions and main function as well to keep the program simple.
# Using list as data structure, since it offers built in functions and seems most feasible.
# Since question doesn't specify anything about negative integers, hence assuming that they are valid input.
# Duplicate pairs will not be considered.


print("Welcome to number pair generator!")
number_list = []  # to hold list of numbers
pairs = []  # List to hold successful pairs

# Taking input from user
while True:
    input_number = int(input("Enter the number in the list. Enter 99999 to exit"))
    if input_number != 99999:
        number_list.append(input_number)
    elif input_number == 99999:
        break

# Determining pairs of numbers whose product is even and sum is odd.
# Append the number pair to list if above criteria is satisfied
i = 0  # Initial index
while i < len(number_list) - 1:
    j = i + 1
    while j < len(number_list):
        num1 = number_list[i]
        num2 = number_list[j]
        if (num1 * num2) % 2 == 0 and (num1 + num2) % 2 != 0:     # Validating the condition
             pairs.append(num1)              # Appending numbers to the pairs list which satisfies the criteria
             pairs.append(num2)
        j += 1
    i += 1

# Removing duplicate pairs from the list, by capturing the pairs and comparing it with the other pair.
k = 0
while k <= len(pairs) - 4:  # Pick numbers until 4th last position, since we are capturing the pairs
    num1 = pairs[k]         # pairs
    num2 = pairs[k + 1]
    m = k + 2
    while m <= len(pairs) - 2:  # Go until second last index
        num3 = pairs[m]
        num4 = pairs[m + 1]
        if (num1 == num3 and num2 == num4) or (num1 == num4 and num2 == num3):  # Condition that determines duplicates
            pairs.pop(m)                                                       # Removing duplicate pairs
            pairs.pop(m)
            m -= 2                                                              # Adjusting the index
        m += 2
    k += 2

# Printing the pairs of numbers.
print("List of pair of numbers whose product is even and sum is odd is: ")
for index in range(0, len(pairs) - 1, 2):
    print("[" + str(pairs[index]) + "," + str(pairs[index + 1]) + "] ", end="")
