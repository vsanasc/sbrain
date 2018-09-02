from .dedication import DedicationSerializer
from .note import NoteSerializer
from .task import TaskSerializer
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
            'tasks': TaskSerializer.dataclass_to_dict(
                                date.tasks
                            ),
            'schedules': ScheduleSerializer.dataclass_to_dict(
                                date.schedules
                            )
        }
