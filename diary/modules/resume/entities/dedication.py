
import datetime


class BaseDedicationEntity(object):

    def __init__(self, name, dedications):
        self._type_name = name
        self._dedications = dedications

    @property
    def type_name(self):
        return self._type_name

    @property
    def dedications(self):
        return self._dedications


class DedicationEntity(object):

    def __init__(self, cycle, time, tags):
        self._cycle = cycle
        self._time = time
        self._tags = tags
        self._total_minutes = cycle * time
        self._total_time = str(
            datetime.timedelta(
                minutes=self._total_minutes
            )
        )

    @property
    def cycle(self):
        return self._cycle

    @property
    def time(self):
        return self._time

    @property
    def tags(self):
        return self._tags

    @property
    def total_minutes(self):
        return self._total_minutes

    @property
    def total_time(self):
        return self._total_time
