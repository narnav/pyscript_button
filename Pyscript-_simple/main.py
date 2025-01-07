print("Hello, World!")

from pyscript import document,display
from datetime import datetime

# function for testing
def test(e):
    print( e.target )
    now = datetime.now()
    display(now.strftime("%m/%d/%Y, %H:%M:%S"))
    print(now)
    document.getElementById('test_button').style.color = 'red'

# set up "Test Button" on interface to perform test
b = document.getElementById('test_button')
b.onclick = test