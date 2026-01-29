class math:
    def mul(self,a,b):
        self.a = a
        self.b = b
        return self.a * self.b
    
    def div(self,a,b):
        self.a = a
        self.b = b
        return self.a / self.b
    
obj = math()
print(obj.mul(4,5))
print(obj.div(20,4))