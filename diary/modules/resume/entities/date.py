

class DateEntity(object):

    def __init__(self, dedications, notes, habits, schedules):
        self._dedications = dedications
        self._notes = notes
        self._habits = habits
        self._schedules = schedules

    @property
    def dedications(self):
        return self._dedications

    @property
    def notes(self):
        return self._notes

    @property
    def habits(self):
        return self._habits

    @property
    def schedules(self):
        return self._schedules
