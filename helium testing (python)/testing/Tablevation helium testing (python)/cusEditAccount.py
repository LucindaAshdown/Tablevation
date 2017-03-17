"""
This script uses Helium to automatically perform a Google search for the term
"Helium", and opens the Wikipedia article on the subject. If all goes well, it
prints "Test passed!". Otherwise, it prints "Test failed :(".
"""
from helium.api import *

email = ("test@test.com")
password = ("Hello123")

start_chrome("http://www.website.dev/customermenu.html")
click("Edit Account")
write("testing1@testing.com", into="Email Address")
write("User", into="Forename")
write("testing", into="Surname")
write("07492746375", into="Phone number")
click(Button("Save"))
go_to("http://www.website.dev/customermenu.html")

if 'Menu' in get_driver().title:
    print('Test passed! Successfully edited and saved the customers details')
else:
    print('Test failed :(')
kill_browser()

