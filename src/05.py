# Create a while loop that starts with x = 0 and increments
# x until x is equal to 5. Each iteration should print to the console.
print("Question 1")
x = 0
while x < 6:
    print("x = %d" % x)
    x = x+1

# Repeat the previous problem, but the loop will skip printing
# x = 5 to the console but will print values of x from 6 to 10.
print("\nQuestion 2") ## You did not reinitialize the X, so it starts from 5 -1
while x < 10: #CK: Will not print out 10 (-1), and s
    print("x = %d" % x)
    x = x+1

# Create a for loop that prints values from 4 to 10 to the console.
print("\nQuestion 3") # Your variable is i, but your are printing x -2
for i in range(4,11):
    print("x = %d" % x)
