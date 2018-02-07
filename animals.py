class animal(object):
    def __init__(self, name, health):
        self.health = health
        self.name = name
    def walk(self, walks):
        self.walks = walks
        self.health -= 1 * self.walks
        return self
    def run(self, runs):
        self.runs = runs
        self.health -= 5 * self.runs
        return self
    def display_health(self):
        print self.health
class dog(animal):
    def __init__(self, health):
        self.health = 150
    def pet(self, pets):
        self.pets = pets
        self.health += 5 * self.pets
        return self
class dragon(animal):
    def __init__(self,health):
        self.health = 170
        super(dragon, self).display_health() 
        print "Im a dragon" 
    def fly(self, flys):
        self.flys = flys
        self.health -= 10 * self.flys
        return self
        display_health(self)

dog = dog("Pupper")
dog.pet(1)
dog.walk(3).run(2).display_health()

dragon = dragon("Reginald" )
dragon.fly(1)
dragon.walk(3).run(2)

