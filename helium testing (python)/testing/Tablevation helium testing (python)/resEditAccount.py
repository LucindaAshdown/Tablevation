"""
This script uses Helium to automatically perform a Google search for the term
"Helium", and opens the Wikipedia article on the subject. If all goes well, it
prints "Test passed!". Otherwise, it prints "Test failed :(".
"""
from helium.api import *

email = ("test@test.com")
password = ("Hello123")

start_chrome("http://www.website.dev/restaurantmenu.html")
click("Edit Account")
write("01028837465", into="Phone number")
click(Button("Monday to Friday Opening time"))
click("09:30AM")
click(Button("Monday to Friday Closing time"))
click("23:30PM")
click(Button("Saturday Opening time"))
click("10:00AM")
click(Button("Saturday Closing time"))
click("23:00PM")
click(Button("Sunday Opening time"))
click("11:00AM")
click(Button("Sunday Closing time"))
click("22:00PM")
click(Button("Please select the type of food"))
click("Spanish")
write("13", into="Total number of seats")
click(Button("Save"))
go_to("http://www.website.dev/restaurantmenu.html")

if 'Menu' in get_driver().title:
    print('Test passed! Successfully edited the restaurants opening and closing times plus current seats and updated the accounts phone number')
else:
    print('Test failed :(')
kill_browser()

