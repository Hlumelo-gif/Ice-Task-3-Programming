# Question 3
total = 0

# Get the first number
num = int(input("Enter a number (0 to stop): "))

# Keep looping until they enter 0
while num != 0:
total = total + num
# Ask for the next number
num = int(input("Enter a number (0 to stop): "))

print("The total sum is:", total)
