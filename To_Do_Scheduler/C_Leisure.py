class Leisure:

    ## this can be like gym, writing, or things that I want to do that don't necessarily have to
    ## be done but I want to make sure I have time for them
    ## maybe have a way to input how often I want to do these things and it will schedule them in
    ## like if I want to go to the gym 3 times a week it will find time in my schedule to do that
    ## make seperate .py file for other activities

    def __init__(self, activity_type, duration, drive_time, reocurring):
        self.activity_type = activity_type
        self.duration = duration
        self.drive_time = drive_time
        self.reoccuring = reocurring
    
    def get_activity_type(self):
        return self.activity_type
    
    def get_duration(self):
        return self.duration
    
    def get_drive_time(self):
        return self.drive_time
    
    # def reoccuring(self, date):
    #     return 
    