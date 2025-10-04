from datetime import date, time, datetime
import Scheduler
import math


## this is my todo list for myself

## Ideal Functionality

## * Input todos(Due Date, Duration, materials) -> Progress Checkin, Scheduled Time to work on 
    ## Based on how much time it takes the due date and other tasks
    ## And giving me still time to have fun. 
    ## I would like a way to send this to my phone
    ## Find time in between my schedule to do task
    ## Update progress on task
    ## A way to change the due date
    
    ## At beginning (can this be done at work or somewhere else)
## * Close them out when task is done

global Progress_Checkin
global Scheduled_Time

mySchedule = Scheduler

listOfProjects = []
listOfTasks = []

class Tasks:
     
     isTaskDone = False
     durationMultiplier = 1.5

     def __init__(self, name, due_date, project_type, duration):
        ## Given the

        self.name = name
        self.due_date = due_date
        self.project_type = project_type
        self.duration = duration

     def add_Task(self):
         ## So I need to save the names, duedate, project type, and duration
         ## They need to keep that information and when necessary be able to update that information
         ## might want to use touples to store this info
         listOfTasks.append(self.name)
        

     def find_due_date(self):
        ## Todo: from the front end communicate to python so I can find a date
        pass
         

     def exepected_Duration(self):
        ## finds expected duration for a project because my brain be straight lying
        expected_duration = self.duration * mySchedule ## need to fix this this shit ain't working
        return expected_duration


     def progress_Checkin_function(self):
        ## has a progress checkin based on duedate, projecttype and expected duration
        ## if it is a task maybe only checkin to see if it is complete
        pass

     def set_up_time(self):
        ## time to set something up really depending on project type and materials
        ## I feel this is more project based than anything 
        pass
    
     def close_Task(self):
        isTaskDone = True
        return isTaskDone




class todos(Tasks):

    ## Todos are something like setting up my credit card, setting up my roth IRA, and things like that
    ## Some household tasks are to be included in here

    def __init__(self):
        super.__init__(self.name)
        super.__init__(self.duration)

   
    

class projects: 

    ## for my hundred plus crochet projects, sewing projects, and whatever else I do
    def __init__(self):
        super.__init__(self.name)




class events:

    ## I need to have something to prompt me to do in preparation to this event

    def __init__(self, date, name, location, preparations):
        self.date = date 
        self.name = name
        self.location = location
        self.preparations = preparations
    

    

class otherActivities:

    ## this can be like gym, writing, or things that I want to do that don't necessarily have to

    def __init__(self, activity_type, duration, drive_time):
        self.activity_type = activity_type
        self.duration = duration
        self.drive_time = drive_time


    




