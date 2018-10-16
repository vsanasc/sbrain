from diary.modules.resume.entities import (
    HabitEntity
)

import datetime


class HabitSerializer(object):

    @staticmethod
    def orm_to_dataclass(query):

        values = []

        for t in query:
            values.append(HabitEntity(t.type.name, t.observation))

        return values

    @staticmethod
    def dataclass_to_dict(tasks):
        return [
                {
                    'name': t.name,
                    'text': t.text
                }
                for t in tasks
        ]
