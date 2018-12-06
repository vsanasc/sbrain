
class HabitEntity(object):

    def __init__(self, name, text):
        self._name = name
        self._text = text

    @property
    def name(self):
        return self._name

    @property
    def text(self):
        return self._text
