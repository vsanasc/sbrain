

class ScheduleEntity(object):

    def __init__(self, type_name, time):
        self._type_name = type_name
        self._time = time

    @property
    def type_name(self):
        return self._type_name

    @property
    def time(self):
        return self._time
