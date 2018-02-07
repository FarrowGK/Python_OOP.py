class cars(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.displayall()
    def displayall(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax
        return self
ferrari = cars("$200,000", "212MPH", "High Octane Race Fuel,", "12MPG")
lamborghini = cars("$150,000", "225MPH", "High Octane Race Fuel,", "10MPG")
gtr = cars("$175,000", "208MPH", "E85", "21 MPG")
chevelle = cars("$50,000", "172MPH", "Premium", "9MPG")
charger70 = cars("$65,000", "192MPH", "Premium", "8MPG")
prius = cars("$25,000", "12MPH", "U Wot m8", "It Never ends")
feet = cars("$0", "4MPH", "Yum", "70-80Years")