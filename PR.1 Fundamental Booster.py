print("Welcome to the Interactive Personal Data Collector!\n")

name = input("Please enter your name: ")
age = int (input("Please enter your age: "))
height = float (input("Please enter your height in meters: "))
favourite_number = int (input("Please enter your favourite number: "))

print("\nThank you! Here is the information we collected:\n")

print("Name:",name, "(Type:", type(name), ", Memory Address:",id(name),")")
print("Age:", age, "(Type:", type(age), ", Memory Address:",id(age),")")
print("Height:", height, "(Type:", type(height), ", Memory Address:",id(height),")")
print("Favourite Number:",favourite_number, "(Type:", type(favourite_number), ", Memory Address:",id(favourite_number),")")

current_year = 2026
birth_year = current_year - age
print("\nYour birth year is approximately: ", birth_year, "(based on your age of", age, ")\n")
print("Thank you for using the Personal Data Collector. Goodbye!") 