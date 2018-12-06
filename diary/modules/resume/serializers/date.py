from .dedication import DedicationSerializer
from .note import NoteSerializer
from .habit import HabitSerializer
from .schedule import ScheduleSerializer


class DateSerializer(object):

    @staticmethod
    def serialize(date):

        return {
            'dedications': DedicationSerializer.dataclass_to_dict(
                                date.dedications
                            ),
            'notes': NoteSerializer.dataclass_to_dict(
                                date.notes
                            ),
            'habits': HabitSerializer.dataclass_to_dict(
                                date.habits
                            ),
            'schedules': ScheduleSerializer.dataclass_to_dict(
                                date.schedules
                            )
        }
