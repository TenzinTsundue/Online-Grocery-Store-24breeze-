# Here is the code to compile all the orders into a single file 

import pandas as pd
import smtplib 

MY_EMAIL = "yourgmail@gmail.com"
MY_PASSWORD = "yourpassword"

# Step 1. Convert the Packing slip into readible file (JSON preferred)

dict1 = {"tomato":4, "banana": 12, "orange": 2}
dict2 = {"graps": 2, "banana": 12, "onion": 2, "tomato": 2}


# Step 2. Compile all order into a single order as a result
def mergeDict(dict1, dict2):
   ''' Merge dictionaries and keep values of common keys in list'''
   dict3 = {**dict1, **dict2}
   for key, value in dict3.items():
       if key in dict1 and key in dict2:
               dict3[key] = [value , dict1[key]]
   return dict3


# Merge dictionaries and add values of common keys in a list
dict3 = mergeDict(dict1, dict2)

print(dict3)

# Step 3. send the result in the mail

with smtplib.SMTP("smtp.gmail.com") as connection:
		connection.starttls()
		connection.login(MY_EMAIL, MY_PASSWORD)
		connection.sendmail(
			from_addr=MY_EMAIL, 
			to_addrs=birthday_person["email"], 
			msg=f"Subject:To Buy!\n\n{dict3}"s
		)