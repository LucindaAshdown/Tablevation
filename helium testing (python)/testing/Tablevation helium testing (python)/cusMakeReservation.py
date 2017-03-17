"""
This script uses Helium to automatically perform a Google search for the term
"Helium", and opens the Wikipedia article on the subject. If all goes well, it
prints "Test passed!". Otherwise, it prints "Test failed :(".
"""
from helium.api import *

email = ("test@test.com")
password = ("Hello123")

start_chrome("http://www.website.dev/customermenu.html")
click("Make Booking")
click(Button("Please a time"))
click("14:30PM")
write("03/23/2017", into="Reservation date")
write("6", into="Total number of seats")
write("I have a nut allergy", into="Extra details")
click(Button("Submit"))
go_to("http://www.website.dev/customermenu.html")

if 'Menu' in get_driver().title:
    print('Test passed! Successfully submitted a reservation')
else:
    print('Test failed :(')
kill_browser()

