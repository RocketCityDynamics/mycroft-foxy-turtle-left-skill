from mycroft import MycroftSkill, intent_file_handler


class MycroftFoxyTurtleLeft(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('left.turtle.foxy.mycroft.intent')
    def handle_left_turtle_foxy_mycroft(self, message):
        self.speak_dialog('left.turtle.foxy.mycroft')


def create_skill():
    return MycroftFoxyTurtleLeft()

