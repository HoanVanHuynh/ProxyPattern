# Let's understand the pattern with a simple example.
# Consider the example of an Actor and his Agent. 
# When production houses want to approach an Actor for a movie, typically, 
# they talk to the Agent and not to the Actor directly.
# Based on the schedule of the Actor and other engagements
# the Agent gets back to the production house on the availability 
# and interest in working in the movie.
# Now, int this scenario, instead of production houses directly talking to the Actor, 
# the Agent acts as a Proxy that
# handles all the scheduling & payments for the Actor. 
# The following Python code implements this scenario where the Actor is the Proxy.
# The Agent object is used to find out if the Actor is busy.
# If the Actor is busy, the Actor().occupied() method is called
# and if the Actor is not busy, the Actor().available() method gets returned.

class Actor(object):
    def __init__(self):
        self.isBusy = False 
    
    def occupied(self):
        self.isBusy = True 
        print(type(self).__name__, 'is occupied with current movie')

    def available(self):
        self.isBusy = False #
        print(type(self).__name__, 'is free for the movie')        

    def getStatus(self):
        return self.isBusy 

class Agent(object):
    def __init__(self):
        self.principal = None 
    
    def work(self):
        self.actor = Actor() 
        if self.actor.getStatus(): 
            self.actor.occupied() 
        else:
            self.actor.available() 

if __name__ == '__main__':
    r = Agent() 
    r.work()