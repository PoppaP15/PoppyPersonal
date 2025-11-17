# from datetime import date, time, datetime
# from Project_Type import projectType
from C_Tasks import task
from C_Events import events
from C_Leisure import Leisure
# import math

class Scheduler:

    ## This also ain't right man so please fix it BITCH


    def __init__(self):
        self.myTasks = []
        self.myEvents = []
        self.myActivities = []

        self.InputTask = task(name="", due_date="", duration="")
        self.InputEvent = events()
        self.InputLeisure = Leisure()
        ## may need a  month and year of something like that
        pass
    ## This definetly not right man
 
    def add_item(self, inputItem):
        if isinstance(inputItem, events):
            self.myEvents.append(inputItem)
        elif isinstance(inputItem, Leisure):
            self.myActivities.append(inputItem)
        else:
            self.myTasks.append(inputItem)

    def get_upcoming(self):
        sortedEvents = sorted(self.myEvents, key=lambda x: x.due_date)
        sortedTasks = sorted(self.myTasks, key=lambda x: x.due_date)
        sortedActivities = sorted(self.myActivities, key=lambda x: x.due_date)
        ## need to figure out a way to return multiple lists
        return print("Upcoming Events: " + sortedEvents, 
                     "Upcoming Tasks: " + sortedTasks, 
                     "Upcoming Activities: " + sortedActivities)
    def make_reoccuring(self):
        return 


# if __name__ == "__Scheduler__" :
Scheduler()
Scheduler.add_item(events("Vegas",1,"need to do shit"))
Scheduler.add_item(Leisure(8,0,True))
Scheduler.add_item(task("2/3/26", 1,6))
Scheduler.get_upcoming()

    



