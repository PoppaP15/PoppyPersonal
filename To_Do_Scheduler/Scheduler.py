from datetime import date, time, datetime
from Project_Type import projectType
from Tasks import task
from Events import events
from To_Do_Scheduler.Leisure import Leisure
import math

class Scheduler:

    ## This also ain't right man so please fix it BITCH


    def __init__(self):
        self.myTasks = []
        self.myEvents = []
        self.myActivities = []

        self.InputTask = task()
        self.InputEvent = events()
        self.InputLeisure = Leisure()
        ## may need a  month and year of something like that
        pass
    ## This definetly not right man
    def add_item(self, item):
        if isinstance(item, events):
            self.myEvents.append(item)
        if isinstance(item, Leisure):
            self.myActivities.append(item)
        if isinstance(item, task):
            self.myTasks.append(item)

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


    

