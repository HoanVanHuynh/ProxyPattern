# https://rednafi.github.io/digressions/python/2020/06/16/python-proxy-pattern.html
# The Proxy Pattern 
# Before diving into the academic definition, let's try to understand the Proxy pattern from an example.
# Have you ever used an access card to go through a door?
# There are multiple options to open that door i.e. 
# It can be opened either using access card or by pressing a button that bypasses the security.
# The door's main functionality is to open 
# but there is a proxy added on top of it
# to add some functionality.

# Let me better explain it using the code example below. 

class Door:
    def open_method(self):
        pass 

class SecuredDoor:
    def __init__(self):
        self._klass = Door() 
    def open_method(self):
        print(f'Adding security measure to the method of {self._klass}')

secured_door = SecuredDoor()
secured_door.open_method()

# Here, the Door class has a single method called open_method 
# which denotes the action of        