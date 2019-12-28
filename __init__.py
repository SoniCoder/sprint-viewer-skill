from mycroft import MycroftSkill, intent_file_handler
from datetime import datetime
from datetime import timedelta
import pytz
import math

class SprintViewer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('viewer.sprint.intent')
    def handle_viewer_sprint(self, message):
        base_sprint = 78
        base_sprint_date = datetime(2019, 4, 1, 0, 0, 0)
        cur_date = datetime.now(pytz.utc) + timedelta(minutes=30, hours=5)
        months_passed = cur_date.month - base_sprint_date.month
        current_sprint = base_sprint + months_passed*2 + math.floor((cur_date.day)/16)
        self.speak("this is sprint %d" % current_sprint)


def create_skill():
    return SprintViewer()

