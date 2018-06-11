

class DateEntity(object):

    def __init__(self, dedications, notes, tasks, schedules):
        self._dedications = dedications
        self._notes = notes
        self._tasks = tasks
        self._schedules = schedules

    @property
    def dedications(self):
        return self._dedications

    @property
    def notes(self):
        return self._notes

    @property
    def tasks(self):
        return self._tasks

    @property
    def schedules(self):
        return self._schedules
