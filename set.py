#Sets are unordered collections of unique elements in Python. 
#They are often used when you need to work with a collection of 
#items where duplicates are not allowed, 
#or when you need to perform set operations like union and intersection.

# Create a set
cars = {"nissan", "toyota", "honda", "ferrari"}

# Add an element to the set
cars.add("mclaren")

# Remove an element from the set
cars.remove("honda")

# Check if an element is in the set
contains_nissan = "nissan" in cars
contains_toyota = "toyota" in cars

# Iterate through the set
print("cars:")
for car in cars:
    print(car)

# Create another set
sport_car = {"mclaren", "ferrari", "lamborghini"}

# Perform set operations
union_sport_car = cars.union(sport_car)
intersection_sport_car = cars.intersection(sport_car)
difference_sport_car = cars.difference(sport_car)

# Print the results
print("Contains 'nissan'? ", contains_nissan)
print("Contains 'toyota'? ", contains_toyota)
print("Union of cars and sport cars:", union_sport_car)
print("Intersection of cars and sport cars:", intersection_sport_car)
print("Difference between cars and sport cars:", difference_sport_car)
