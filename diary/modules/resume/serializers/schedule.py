from diary.modules.resume.entities import (
    ScheduleEntity
)

import datetime


class ScheduleSerializer(object):

    @staticmethod
    def orm_to_dataclass(query):

        values = []

        for t in query:
            values.append(ScheduleEntity(t.type.name, t.time))

        return values

    @staticmethod
    def dataclass_to_dict(schedules):
        return [
                {
                    'name': t.type_name,
                    'time': t.time
                }
                for t in schedules
        ]
