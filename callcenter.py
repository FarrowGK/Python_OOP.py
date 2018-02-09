import datetime
import uuid
time = datetime.datetime.now()
calls = []
class call(object):
    def __init__(self, ids, name, number, time, reason):
        self.ids = ids
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    def display(self):
        print "Your unique id is: {}\n Name: {}\n Number: {}\n Time Accessed: {}\n Reason for Calling: {} \n".format(self.ids, self.name, self.number, self.time, self.reason)
        return self
class callcenter(call):
    def __init__(self, ids, name, number, time, reason):
        self.ids = ids
        self.ids = ids
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
        self.list = []
        self.qsize = len(calls)
    def add(self):    
        self.list = [self.ids, self.name, self.number, self.time, self.reason]
        calls.append(self.list)
    def remove(self):
        calls.pop(0)
        return self
    def info(self):
        print "The que length is {} people and consists of {} at {}".format(len(calls), self.name, self.number)
        return self

clientA = callcenter(uuid.uuid4(), "Ronald", "7037895608", time, "I want to call")
clientA.add()
clientA.display()
clientA.info()
clientB = callcenter(uuid.uuid4(),"Kate", "7037912524", time, "Im lonely")
clientB.add()
clientB.display()
clientB.info()
clientB.remove()

