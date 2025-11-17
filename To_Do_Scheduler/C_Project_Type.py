from datetime import date, time, datetime
from C_Tasks import task, projects, todos



class projectType(projects):

    ## this might need to be a subclass of projectType

    ## Will have a string that will be passed through 
    # Depending on that string it will have it's own multiplier
    
    def __init__(self, name, time_multiplier, material, due_date, duration):

        super.__init__(self, name, due_date, duration)
        self.time_multiplier = time_multiplier
        self.material = material

    def get_name(self):
        pass

    def get_Multiplier(self):
        if self.name == "crochet":
            durationMultiplier = 1.75
        if self.name == "painting":
            durationMultiplier = 2
        if self.name == "sewing":
            durationMultiplier = 2.3
        return durationMultiplier
    
## Might need this might not just depending on what I want to do 
    
# class crochet(projectType):

#     def __init__(self):
#         super.__init__(self.name)

    
        
        

