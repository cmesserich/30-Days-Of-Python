first_name = "chris"
last_name = "messerich"
full_name = first_name + last_name
country = "US" 
city = "omaha" 
age = 28
year = 2026
is_married = False
is_true = True
is_light = True

multipe, variable_name, superstar = 10, "yessir", "ME"

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))

print(len(first_name))
print(len(last_name))
len_result_first_longer = len(first_name) > len(last_name)
print("The length of the first name is longer than the last name:", len_result_first_longer)

num_one = 5
num_two = 4

total = num_one + num_two
print(total)
diff = num_one - num_two
print(diff)
product = num_one * num_two
print(product)
division = num_one / num_two
print(division)
remainder = num_one % num_two
print(remainder)
exp = num_one ** num_two
print(exp)
floor = num_one // num_two
print(floor)
r = 30 
print(r)
area_of_circle = 3.14 * r * r 
print(area_of_circle)
circum_of_circle = 3.14 * 2 * r 
print(circum_of_circle)
r_user = input("Enter a number: ")
try:
    r_user = int(r_user)
    print(r_user)
    print(area_of_circle)
except ValueError:
    print("Invalid input. Please enter a valid number.")
