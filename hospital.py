import uuid
patients = []
class Hospital(object):
    def __init__(self):
        self.hname = "Seattle Grace Mercy West"
        self.capacity = 3
    def admit(self):
        if len(patients) < self.capacity:
            patients.append(self.pname)
            self.bednumber = patients.index(self.pname)
            print patients
            print self.ids, self.pname, self.ailment, self.bednumber
        else:
            print "Sorry bud your SOL", self.bednumber
    def discharge(self):
        self.kickedout = patients.index(self.pname)
        patients.pop(self.kickedout)
class Patients(Hospital):
    def __init__(self, ids, pname, ailment):
        super(Patients,self).__init__()
        self.ids = ids
        self.pname = pname
        self.ailment = ailment
        self.bednumber = "You do not have a bed yet"
patient1 = Patients(uuid.uuid4(), "Reggie", "No Rings")
patient2 = Patients(uuid.uuid4(), "Ray", "Steph")
patient3 = Patients(uuid.uuid4(), "Steph", "Not enough 3's")
patient4 = Patients(uuid.uuid4(), "Shaq", "Jackson")
patient1.admit()
patient2.admit()
patient3.admit()
patient4.admit()
print patients
patient1.discharge()
print patients
