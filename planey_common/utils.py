import datetime

from django.conf import settings
import pendulum
from pendulum import DateTime, Date


def get_now(tz=settings.TIME_ZONE) -> DateTime:
    """Get current pendulum datetime instance of default timezone

    Returns:
        DateTime
    """
    return pendulum.now(tz)


def get_date_from_pendulum_date(date: Date) -> Date:
    return datetime.date(year=date.year, month=date.month, day=date.day)
