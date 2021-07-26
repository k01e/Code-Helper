### String Manuplication ###
# Reverse String
reverseString = "Test String"
print(reverseString[::-1])

# String Substring
subString = "freeCodeCamp"
print(subString[0:5])

# String Find
# string.find(value, start, end) # Returns char location
findString = "Hey kid, I'm a computer."
print(findString.find('kid'))

# String Length
lengthString = "freeCodeCamp"
print(len(lengthString))

# String Split
splitString = "Line 1 \n Line 2"
print(splitString)
print(splitString.replace(" ", "").split("\n"))

# Remove Whitespace
whSpString = " Test Test Test    "
print(whSpString.strip())

# Place Holder
placeHolderString = "Test{} Test{} Test{}"
print(placeHolderString.format(1,2,3))

##########################
# Parse String into JSON #

str = "Assignment Number=484537       Employee Name=John Smith           Location=London\n  Assignment Number=859375       Employee Name=Fatima Ali           Role=Manager\n"

# print(x)

# Using Split and Substring
records = str.split("\n")
# print(str.split("\n"))

x =  1
json = ""

for rec in records:
    record = ""
    
    if x > 1:
        record += ","
    
    assNumberStart = rec.find("Assignment Number") + 19
    assNumberEnd = assNumberStart + 8
    # print("{} {}".format(assignmentNumberStart, assignmentNumberEnd))
    
    assNumber = rec[assNumberStart:assNumberEnd].rstrip()
    # print(assNumber)
    
    empNameStart = rec.find("Employee Name") + 14
    empNameEnd = empNameStart + 12
    
    empName = rec[empNameStart:empNameEnd].rstrip()
    # print(empName)
    
    record += "{\"Assignment Number\":\""+ assNumber +"\", \"Employee Name\":\""+ empName +"\""
    
    if "Location" in rec:
        locStart = rec.find("Location") + 9
        locEnd = locStart + 6
    
        loc = rec[locStart:locEnd]
        # print(loc)
        
        record += ", \"Location\":\""+ loc +"\""
        
    if "Role" in rec:
        roleStart = rec.find("Role") + 5
        roleEnd = roleStart + 9
    
        role = rec[roleStart:roleEnd]
        # print(role)
        
        record += ", \"Role\":\""+ role +"\""
    
    # print(rec)
    # record = "{ \"Assignment Number\":\"{}\" }"
    # print (record + "}")
    json += record + "}"
    x += 1

print("[" + json + "]")

# Using Replace
print(str.rstrip().replace("=", "\": \"").replace("       ", "\",\""))


###################
# def say_hello():
#     print('Hello, World')

# for i in range(5):
#     say_hello()
