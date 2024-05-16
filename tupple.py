# Create a tuple
cars = ("nissan", "toyota", "honda", "ferrari")

( "a" , 1 , 2 , "b"    )




# Access elements by index
first_car = cars[0]
second_car = cars[1]

# Iterate through the tuple
print("Cars:")
for car in cars:
    print(car)

# Check if an element is in the tuple
contains_honda = "honda" in cars

# Find the length of the tuple
num_cars = len(cars)

# Concatenate two tuples
more_cars = ("lamborghini", "mclaren")
all_cars = cars + more_cars

# Nested tuple
nested_tuple = ("red", ("green", "white"))

# Print the results
print("First car:", first_car)
print("Second car:", second_car)
print("Does it contain 'honda'? ", contains_honda)
print("Number of cars:", num_cars)
print("All cars:", all_cars)
print("Nested tuple:", nested_tuple)
