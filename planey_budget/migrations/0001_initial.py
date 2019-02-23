# Generated by Django 2.1.7 on 2019-02-23 12:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='수정 일시')),
                ('deleted_at', models.DateTimeField(default=None, help_text='삭제 일시', null=True)),
                ('date', models.DateField(default=datetime.date(2019, 2, 1))),
                ('amount', models.PositiveIntegerField(default=0, help_text='해당 달 할당 금액')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='수정 일시')),
                ('deleted_at', models.DateTimeField(default=None, help_text='삭제 일시', null=True)),
                ('name', models.CharField(help_text='이름', max_length=140)),
                ('month_amount', models.PositiveIntegerField(default=0, help_text='매 달 할당 금액')),
                ('total_amount', models.PositiveIntegerField(default=0, help_text='총 금액')),
                ('goal_amount', models.PositiveIntegerField(default=0, help_text='목표 금액', null=True)),
                ('due_date', models.DateTimeField(help_text='마감 날짜', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='budget',
            name='plan',
            field=models.ForeignKey(help_text='계획', on_delete=django.db.models.deletion.DO_NOTHING, related_name='budgets', to='planey_budget.Plan'),
        ),
    ]
