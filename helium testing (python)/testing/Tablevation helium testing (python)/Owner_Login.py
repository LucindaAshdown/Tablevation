"""
This script uses Helium to automatically perform a Google search for the term
"Helium", and opens the Wikipedia article on the subject. If all goes well, it
prints "Test passed!". Otherwise, it prints "Test failed :(".
"""
from helium.api import *




start_chrome("website.dev")
click("Login")
write("test@test.com", into="Email Address")
write("Hello12", into="Password")
click("Owner")
click(Button("Login"))
go_to("http://www.website.dev/restaurantmenu.html")
if 'Menu' in get_driver().title:
	print('Test passed! Successfully logged into the restaurant account')
else:
	print('Test failed :(')
kill_browser()
