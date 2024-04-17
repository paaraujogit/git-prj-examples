"""
Data Science - Menu Object Oriented - paaraujo@gmail.com
  * Object Oriented Version *
    - Class Menu
"""

class Menu:
    def __init__(self):
        self.options=[]    
        self.methods=[]
        self.msg=""
    def setOptions(self, opts):
        self.options=opts
        self.num_opts=len(self.options)-1
        if self.num_opts<0:
            self.num_opts=0
    def setMethods(self, mtds):
        self.methods=mtds
    def setMsg(self, msgl):
        self.msg=msgl
    def once(self):         # execute one option and return
        if self.num_opts == 0:
            print("Menu sem opcoes.")
            return
        ops=range(1,self.num_opts+1)
        for op in self.options:
            print(op)
        print(self.msg, [*ops], ":", end=' ')
        op = Menu.getIntVals(1, self.num_opts)
        self.execute(op)
        return op
    def loop(self):
        op=self.once()
        while op != self.num_opts:
            op=self.once()
    def execute(self, op):
        if self.methods[op] == 0:  # Option not implemented or return
            if op != self.num_opts:
                print("Not implemented")
            return
        else:
            self.methods[op]()
    @staticmethod
    def getInt():
        valid = False
        while not valid:
            try:
                ret = int(input())
                if ret >= 0:
                    return ret
                print("not valid: ", end='')
            except ValueError:
                print("not valid: ", end='')
    @staticmethod
    def getIntMsg(msg):
        print(msg, end='')
        return Menu.getInt()
    @staticmethod
    def getIntVals(min, max):
        valid = False
        while not valid:
            ret = Menu.getInt()
            if ret >= min and ret <= max:
                return ret
            print("not valid: ", end='')