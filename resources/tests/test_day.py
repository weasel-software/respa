import datetime

from django.test import TestCase
from resources.models import *


class DayTestCase(TestCase):
    """
    # Test case for day handler

    Creates a week of regular period with open hours and two day closed exceptional period

    Tests that day creation works as it should
    """

    def setUp(self):
        u1 = Unit.objects.create(name='Unit 1', id='unit_1')
        u2 = Unit.objects.create(name='Unit 2', id='unit_2')
        rt = ResourceType.objects.create(name='Type 1', id='type_1', main_type='space')
        Resource.objects.create(name='Resource 1a', id='r1a', unit=u1, type=rt)
        Resource.objects.create(name='Resource 1b', id='r1b', unit=u1, type=rt)
        Resource.objects.create(name='Resource 2a', id='r2a', unit=u2, type=rt)
        Resource.objects.create(name='Resource 2b', id='r2b', unit=u2, type=rt)

        # Regular hours for one week
        p1 = Period.objects.create(start=datetime.date(2015, 8, 3), end=datetime.date(2015, 8, 9), unit=u1, name='regular hours')
        Day.objects.create(period=p1, weekday=0, opens=datetime.time(8, 0), closes=datetime.time(18, 0))
        Day.objects.create(period=p1, weekday=1, opens=datetime.time(8, 0), closes=datetime.time(18, 0))
        Day.objects.create(period=p1, weekday=2, opens=datetime.time(8, 0), closes=datetime.time(18, 0))
        Day.objects.create(period=p1, weekday=3, opens=datetime.time(8, 0), closes=datetime.time(18, 0))
        Day.objects.create(period=p1, weekday=4, opens=datetime.time(8, 0), closes=datetime.time(18, 0))
        Day.objects.create(period=p1, weekday=5, opens=datetime.time(12, 0), closes=datetime.time(16, 0))
        Day.objects.create(period=p1, weekday=6, opens=datetime.time(12, 0), closes=datetime.time(14, 0))

        # Two shorter days as exception
        exp1 = Period.objects.create(start=datetime.date(2015, 8, 6), end=datetime.date(2015, 8, 7), unit=u1,
                                     name='exceptionally short days', exception=True, parent=p1)
        Day.objects.create(period=exp1, weekday=3,
                           opens=datetime.time(12, 0), closes=datetime.time(14, 0))
        Day.objects.create(period=exp1, weekday=4,
                           opens=datetime.time(12, 0), closes=datetime.time(14, 0))

        # Weekend is closed as an exception
        exp2 = Period.objects.create(start=datetime.date(2015, 8, 8), end=datetime.date(2015, 8, 9), unit=u1,
            name='weekend is closed', closed=True, exception=True, parent=p1)

    def test_days(self):
        periods = Period.objects.all()
        self.assertEqual(len(periods), 3)

