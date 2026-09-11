# Question 1
secret = 65
guess = 0

# Keep looping until they guess the correct number
while guess != secret:
guess = int(input("Guess the number: "))

if guess < secret:
print("Too low!")
elif guess > secret:
print("Too high!")

print("Correct! You guessed the number.")
