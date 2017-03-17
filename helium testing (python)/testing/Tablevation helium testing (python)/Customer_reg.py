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
click("Create Customer Account")
write(email, into="Email Address")
write(password, into="Password")
write("jamie", into="First Name")
write("testing", into="Surname")
write("02029937485", into="Phone number")
click(Button("Register"))
write(email, into="Email Address")
write(password, into="Password")
click("Customer")
click(Button("Login"))

if 'Home' in get_driver().title:
    print('Test passed! Successfully created and logged into a customer account')
else:
    print('Test failed :(')
kill_browser()

