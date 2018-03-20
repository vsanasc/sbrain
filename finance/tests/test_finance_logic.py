from django.test import TestCase


class TestViews(TestCase):

    def setUp(self):
        pass

    def test_basic(self):
        a = 1
        self.assertEqual(1, a)
