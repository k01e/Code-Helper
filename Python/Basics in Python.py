############
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names[0])    # John
print(names[-1])   # Mary
print(names[0:3])  # ['John', 'Bob', 'Mosh']

names.append("Josh")
print(names)       # ['John', 'Bob', 'Mosh', 'Sam', 'Mary', 'Josh']

names.insert(3, "Katie")
print(names)       # ['John', 'Bob', 'Mosh', 'Katie', 'Sam', 'Mary', 'Josh']

##################
i = 1
while i <= 10:
    print(i * '*')
    i += 1

##################
# Fun with Ranges #
x = range(0,10,2)
print(list(x))   # [0, 2, 4, 6, 8]

y = range(50,40,-1)
print(list(y))   # [50, 49, 48, 47, 46, 45, 44, 43, 42, 41]

####################
# Weight Converter #
weight = input("Weight: ")
unit = input("(K)g or (L)bs: ")

if unit.upper() == "L":
    print("Weight in Kg: " + str(float(weight) * 0.45))
else:
    print("Weight in Lbs: " + str(float(weight) / 0.45))

###############
# Sum Numbers #
val1 = input("First: ")
val2 = input("Second: ")

print("Sum: " + str(float(val1) + float(val2)))

##############
# Print Name #
name = input("What is your name? ")
print("Hello ", name)

