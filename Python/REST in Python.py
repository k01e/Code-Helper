# Standard GET call

import requests

url = "https://cat-fact.herokuapp.com/facts"

payload={}
headers = {
  'Cookie': 'connect.sid=s%3Ahbpmw48zJNNHfxo5RsFsrPLK2sxRDdC-.vtbYBMY6kjxi7a6c0eIU4FdnK8hpr0EHfYFG0riaMQc'
}

response = requests.request("GET", url, headers=headers, data=payload)

# print(type(response.text)) # str
# print(len(response.text)) # 1859
# print(response.text)

# Find text in string

loc = response.text.find("text") + 7 # to remove key
end = response.text.find("?", 140) + 1 # to include the punctuation
print(loc)
print(end)
# print(type(loc))

fact = response.text[loc:end]
print(fact)



############
# def say_hello():
#     print('Hello, World')
#
# for i in range(5):
#    say_hello()
