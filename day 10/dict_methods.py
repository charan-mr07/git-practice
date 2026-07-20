# Dictionary Methods (common ones)
student = {"name": "Charan", "age": 18, "course": "ECE"}

print(student.get("name"))           # access value (safe way)
print(student.get("college", "N/A")) # if key doesn't exist, gives a default value

student.update({"college": "Aditya"})  # add/update a new key-value pair
student["year"] = 1                    # direct add also works

print(student.keys())     # shows all keys
print(student.values())   # shows all values
print(student.items())    # shows all key-value pairs as tuples

student.pop("age")        # removes a specific key
print(student)

for key, value in student.items():   # loop through the dictionary
    print(key, ":", value)

# get() vs direct access — important difference 

 student = {"name": "Charan"}

print(student["age"])        # gives an ERROR (key doesn't exist)
print(student.get("age"))    # gives None (no error, safe way)
print(student.get("age", 18)) # gives the default value, no error either  
#.get() prevents your program from crashing.