from django.db import models

from planey_common.models import BaseModel
from planey_common.utils import get_now, get_date_from_pendulum_date


class Plan(BaseModel):
    """예산 계획"""

    name = models.CharField(max_length=140, help_text="이름")
    month_amount = models.PositiveIntegerField(default=0, help_text="매 달 할당 금액")
    total_amount = models.PositiveIntegerField(default=0, help_text="총 금액")
    goal_amount = models.PositiveIntegerField(default=0, null=True, help_text="목표 금액")
    due_date = models.DateTimeField(null=True, help_text="마감 날짜")

    def __str__(self):
        return self.name


class Budget(BaseModel):
    """매 달 예산"""

    plan = models.ForeignKey('Plan', related_name="budgets", on_delete=models.DO_NOTHING, help_text="계획")
    date = models.DateField(default=get_date_from_pendulum_date(get_now().set(day=1).date()))
    amount = models.PositiveIntegerField(default=0, help_text="해당 달 할당 금액")

    def __str__(self):
        return f"{self.plan} {self.date.strftime('%Y-%m')}"
