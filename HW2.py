try:
    gross = float(input("Enter gross salary: "))
    children = int(input("Enter number of children: "))
except ValueError:
    print("Invalid input. Please, enter numbers only")

# Base tax rate

if gross < 1000:
    tax_rate = 0.1
elif gross < 2000:
    tax_rate = 0.12
elif gross < 4000:
    tax_rate = 0.14
else:
    tax_rate = 0.18

# Applying children tax cut

if gross < 2000:
    tax_rate -= children * 0.01
else:
    tax_rate -= children * 0.005

# Although very unlikely, we must make sure tax rate is not negative:

if tax_rate < 0:
    tax_rate = 0

# Calculate net salary
tax = gross * tax_rate
net = gross - tax

print("Net salary:", net)
