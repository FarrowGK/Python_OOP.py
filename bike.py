class bike(object):
    def __init__(self, price, max_speed, times_ridden, times_reversed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
        self.times_ridden = times_ridden
        self.times_reversed = times_reversed
    def ride(self):
        self.miles += 10 * self.times_ridden
        print "Riding...."
        return self
    def reverse(self):
        self.miles -= 5 * self.times_reversed
        print "Reversing..."
        return self
    def displayinfo(self):
        self.ride()
        self.reverse()
        if self.miles >= 0:
            print self.price,  self.max_speed, self.miles
            return self
        else:
            print self.price,  self.max_speed, self.miles, "Cool Negative Miles teach me to do that"
            return self
            

bike1 = bike("$200.00", "20mph", 3, 1)
bike2 = bike("$150.00", "15 mph", 2, 2)
bike3 = bike("$100.00", "10mph", 0, 3)

#print bike1.price, bike1.max_speed, bike1.miles
print bike1.displayinfo()
print bike2.displayinfo()
print bike3.displayinfo()
