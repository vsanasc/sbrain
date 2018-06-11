from django.contrib.auth.models import User
from diary.modules.resume.entities import (
    DateEntity
)

from diary.modules.resume.serializers import (
    DedicationSerializer,
    NoteSerializer,
    TaskSerializer,
    ScheduleSerializer
)

from diary.models import (
    Dedication,
    Date,
    SmallNote,
    Task,
    Schedule
)

import datetime


class DateDatabaseRepo(object):

    def get_date(self, user, year, month, day):

        dat = datetime.date(year, month, day)

        user_i = User.objects.get(pk=user)
        date_i = Date.objects.filter(user=user_i, date=dat).first()

        dedications = Dedication.objects.filter(date=date_i, status=1)
        notes = SmallNote.objects.filter(date=date_i, status=1)
        tasks = Task.objects.filter(date=date_i, status=1)
        schedules = Schedule.objects.filter(date=date_i, status=1)

        return DateEntity(
            DedicationSerializer.orm_to_dataclass(dedications),
            NoteSerializer.orm_to_dataclass(notes),
            TaskSerializer.orm_to_dataclass(tasks),
            ScheduleSerializer.orm_to_dataclass(schedules)
        )


class DateCacheRepo(object):

    def get_date(self, user, year, month, day):
        return None

    def save_date(self, date):
        pass


class DateRepo(object):

    def __init__(self, db_repo, cache_repo):
        self.db_repo = db_repo
        self.cache_repo = cache_repo

    def get_date(self, user, year, month, day):

        date = self.cache_repo \
                    .get_date(
                        user,
                        year,
                        month,
                        day
                    )

        if date is None:
            date = self.db_repo \
                        .get_date(
                            user,
                            year,
                            month,
                            day
                        )

            self.cache_repo.save_date(date)

        return date
