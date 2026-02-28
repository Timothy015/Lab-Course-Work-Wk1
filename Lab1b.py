# Lab1b Introduction
# Ask user to enter name

print('Enter your name:')
name = input()

# Ask User to Enter Values

print('Enter a value:')
a_str = input()

print('Enter b value:')
b_str = input()

a = int(a_str)
b = int(b_str)

# Perform calculations of the entered values

total = a + b
diff = a - b
prod = a * b
div = a / b

# Display the results of the calculations

print(name, 'your calculations are:')
print(a, '+', b, '=', total)
print(a, '-', b, '=', diff)
print(a, '*', b, '=', prod)
print(a, '/', b, '=', div)

print('The calculations are complete.')
