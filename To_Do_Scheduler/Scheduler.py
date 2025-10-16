from datetime import date, time, datetime
from Project_Type import projectType
from Tasks import task
from Events import events
from Other_Activities import otherActivities
import math

class Scheduler:

    def __init__(self):
        self.myTask = []
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
            self.myTask.append(item)

    def get_upcoming(self):
        ## return sorted(self.myEvents, key=lambda x: x.due_date)
        ## need to figure out a way to return multiple lists
        pass

    

