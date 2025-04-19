# Variables in Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname': 'Asabeneh',
   'lastname': 'Yetayeh',
   'country': 'Finland',
   'city': 'Helsinki'
   }
print('Hello, World!')  # The text Hello, World! is an argument
print('Hello', ',', 'World', '!')  # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!'))  # it takes only one argument
# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Multiple variables can also be declared in one line:
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

# Getting user input using the input() built-in function.
# Let us assign the data we get from a user into first_name and age variables. Example
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

# Checking Data types and Casting
# Different python data types
# Let's declare variables with various data types

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int, it is not my real age, don't worry about it

# Printing out types
print(type('Asabeneh'))          # str
print(type(first_name))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name': 'Asabeneh'})) # dict
print(type((1,2)))               # tuple
print(zip([1,2],[3,4]))    # zip



