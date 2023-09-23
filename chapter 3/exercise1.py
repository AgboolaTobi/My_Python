# Exercise 1. 3.1 (Validating User Input) Modify the script of Fig3.3. to validate its
# inputs. For any input, if the value entered is other than 1 or 2, keep looping
# until the user enters a correct value. Use one counter to keep track of the
# number of passes, then calculate the number of failures after all the user’s
# inputs have been received

passes = 0
count = 0
while inputs != 1:
    inputs = int(input("Enter a number other than 1 (Enter 1 or when you wish to stop): "))
    passes += inputs
    count += 1

print(inputs)
