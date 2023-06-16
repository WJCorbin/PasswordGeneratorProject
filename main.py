import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = ""
rand_number = 0

print("Welcome to the PyPassword Generator!")
password_length = int(input("How many characters would you like in your password total?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_letters = password_length - nr_symbols - nr_numbers

for charater in range(0, password_length):
  if nr_letters == 0 and nr_numbers == 0:
    password += random.choice(symbols)
    nr_symbols -= 1
  elif nr_letters == 0 and nr_symbols == 0:
    password += random.choice(numbers)
    nr_numbers -= 1
  elif nr_numbers == 0 and nr_symbols == 0:
    password += random.choice(letters)
    nr_letters -= 1
  elif nr_symbols == 0:
    rand_number = random.randint(1, 2)
    if rand_number == 1:
      password += random.choice(numbers)
      nr_numbers -= 1
    else:
      password += random.choice(letters)
      nr_letters -= 1
  elif nr_numbers == 0:
    rand_number = random.randint(1, 2)
    if rand_number == 1:
      password += random.choice(symbols)
      nr_symbols -= 1
    else:
      password += random.choice(letters)
      nr_letters -= 1
  elif nr_letters == 0:
    rand_number = random.randint(1, 2)
    if rand_number == 1:
      password += random.choice(symbols)
      nr_symbols -= 1
    else:
      password += random.choice(numbers)
      nr_numbers -= 1
  else:
    rand_number = random.randint(1, 3)
    if rand_number == 1:
      password += random.choice(symbols)
      nr_symbols -= 1
    elif rand_number == 2:
      password += random.choice(numbers)
      nr_numbers -= 1
    else:
      password += random.choice(letters)
      nr_letters -= 1

print(f"Your password is: {password}")