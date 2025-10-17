from datetime import date, time, datetime
from Project_Type import projectType
from Tasks import task
from Events import events
from Other_Activities import otherActivities
import math

class Scheduler:

    def __init__(self):
        self.myTasks = []
        self.myEvents = []
        self.myOtherActivities = []
        ## may need a  month and year of something like that
        pass
# ## This definetly not right man
    def add_item(self, item):
        if isinstance(item, events):
            self.myEvents.append(item)
        if isinstance(item, otherActivities):
            self.myOtherActivities.append(item)
        if isinstance(item, task):
            self.myTasks.append(item)

    def get_upcoming(self):
        sortedEvents = sorted(self.myEvents, key=lambda x: x.due_date)
        sortedTasks = sorted(self.myTasks, key=lambda x: x.due_date)
        sortedOtherActivities = sorted(self.myOtherActivities, key=lambda x: x.due_date)
        ## need to figure out a way to return multiple lists
        return print("Upcoming Events: " + sortedEvents, 
                     "Upcoming Tasks: " + sortedTasks, 
                     "Upcoming Activities: " + sortedEvents)

    

