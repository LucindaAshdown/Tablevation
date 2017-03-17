"""
This script uses Helium to automatically perform a Google search for the term
"Helium", and opens the Wikipedia article on the subject. If all goes well, it
prints "Test passed!". Otherwise, it prints "Test failed :(".
"""
from helium.api import *

#email = raw_input("Email address registered with Tabelvation: ")
#password = raw_input("Password registered with Tabelvation: ")
#fName = raw_input("First name: ")
#sName = raw_input("Surname: ")
#number = raw_input("Phone number for account: ")
email = ("test@test.com")
password = ("Hello123")

start_chrome("website.dev")
click("Create Restaurant Account")
write(email, into="Email Address")
write(password, into="Password")
write("ResTesr", into="Restaurant Name")
write("1 portsmouth road", into="Address Line 1")
click(Button("Please select an Area"))
click("Southsea")
write("po1 1eh", into="Post code")
write("01928374659", into="Phone number")
click(Button("Please select the type of food"))
click("Greek")
write("36", into="Total number of seats")
click(Button("Register"))
write(email, into="Email Address")
write(password, into="Password")
click("Owner")
click(Button("Login"))
go_to("http://website.dev/restaurantmenu.html")

if 'Menu' in get_driver().title:
    print('Test passed! Successfully created and logged into a restaurant account')
else:
    print('Test failed :(')
kill_browser()

