class std:
    def name(self,name):
        self.name = name
        return self.name
    
    def course(self,course):
        self.course = course
        return self.course  
    
obj = std()
obj.name("Harry")
obj.course("B.Tech")