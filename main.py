# Get user input
first_name, last_name, number = input().split()

# Extract the first five letters of the last name (or all if less than five)
last_name_part = last_name[:5]

# Extract the first letter of the first name
first_name_part = first_name[0]

# Extract the last two digits of the number
number_part = number[-2:]

# Combine the parts to create the login name
login_name = last_name_part + first_name_part + number_part

# Output the login name
print(f'Your login name: {login_name}')
