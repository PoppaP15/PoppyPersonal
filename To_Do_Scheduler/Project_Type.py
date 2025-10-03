from datetime import date, time, datetime



class projectType:

    ## Will have a string that will be passed through 
    # Depending on that string it will have it's own multiplier
    
    def __init__(self, name, time_multiplier, material):
        self.name = name
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
    
        
        

