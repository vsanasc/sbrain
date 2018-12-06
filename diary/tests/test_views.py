from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase

from autofixture import AutoFixture

from core.models import Tag

from diary.models import (
    Date,
    Dedication,
    GeneralType,
    Schedule,
    TypeSchedule,
    SmallNote,
    Habit,
    TypeHabit,
)

import datetime


class TestViews(TestCase):

    def setUp(self):

        user = User(email='test@django.com', username='testuser')
        user.set_password('test')
        user.is_staff = True
        user.is_super = True
        user.save()

        today = datetime.date.today()

        date = Date(user=user, date=today)

        AutoFixture(Tag).create(10)
        AutoFixture(TypeTask).create(10)
        AutoFixture(TypeSchedule).create(10)
        AutoFixture(GeneralType).create(10)
        AutoFixture(Date, follow_fk=True).create(10)
        AutoFixture(Schedule, follow_fk=True).create(10)
        AutoFixture(SmallNote, follow_fk=True).create(10)
        AutoFixture(Task, follow_fk=True).create(10)

        self._user = user
        self._date = date
        self._today = today

    def test_diary_without_user(self):

        url = reverse('diary-date', kwargs={
                          'year': self._today.year,
                          'month': self._today.month,
                          'day': self._today.day
                      })

        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)

    def test_diary_with_user(self):

        # Login
        self.client.login(username='testuser', password='test')

        url = reverse('diary-date', kwargs={
                          'year': self._today.year,
                          'month': self._today.month,
                          'day': self._today.day
                      })

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
