class Mathdojo(object):
    def __init__(self):
        pass
    def add(self, addition, *args):
        if type(addition) is list or tuple:           
            self.addition = sum(addition)
            arr1.append(self.addition)
        else:
            self.addition = addition
            arr1.append(self.addition)
        if type(args) is list or tuple and not int:
            self.args = sum(args)
            arr1.append(self.args)
        else:
            self.args = args[0]
            arr1.append(self.args)
        return self
    def result(self):
        self.sumthis = sum(arr1[3])        
        arr1[3] = self.sumthis
        print arr1
        return self
arr1 = []
md = Mathdojo()
md.add([1],3,4).add([3,5,7,8], [2,4.3,1.25]).result()
