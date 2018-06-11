
class BaseNoteEntity(object):

    def __init__(self, name, notes):
        self._role_name = name
        self._notes = notes

    @property
    def role_name(self):
        return self._role_name

    @property
    def notes(self):
        return self._notes


class NoteEntity(object):

    def __init__(self, time, text, featured):
        self._time = time
        self._text = text
        self._featured = featured

    @property
    def time(self):
        return self._time

    @property
    def text(self):
        return self._text

    @property
    def featured(self):
        return self._featured
