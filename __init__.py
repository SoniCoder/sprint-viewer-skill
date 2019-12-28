from mycroft import MycroftSkill, intent_file_handler


class SprintViewer(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('viewer.sprint.intent')
    def handle_viewer_sprint(self, message):
        self.speak_dialog('viewer.sprint')


def create_skill():
    return SprintViewer()

