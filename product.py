class product(object):
    def __init__(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"
    def sell(self):
        self.staus = "Sold"
        return self
    def addtax(self, taxrate):
        self.taxrate = taxrate
        self.price = float(self.price) + (self.taxrate * float(self.price))
        return self
    def returns(self, returnreason):
        self.returnreason = returnreason       
        if self.returnreason == "Defective":
            self.status = "Defective"
            self.price = 0
        elif self.returnreason is "Box Return":
            self.status = "For Sale"
        elif self.returnreason == "Open Box":
            self.status = "Used"
            self.price = self.price - (self.price * .2)
        else:
            self.status = "Returned"
        return self
    def display_info(self):
        print "Your {} {} is ${} and weighs {} and it is {}".format(self.brand, self.name, self.price, self.weight, self.status)
        return self
turbo = product(700, "Turbo", "10Lbs", "HKS")
turbo.addtax(.15)
turbo.returns("Box Return").display_info()






    
    