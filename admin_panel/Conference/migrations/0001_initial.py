# Generated by Django 4.0.6 on 2022-07-31 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название конференции', max_length=500, verbose_name='Название конференции')),
                ('date', models.DateField(help_text='Дата конференции', verbose_name='Дата конференции')),
            ],
            options={
                'verbose_name': 'конференцию',
                'verbose_name_plural': 'Конференции',
            },
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.IntegerField(verbose_name='Телеграм-ID докладчика')),
                ('fullname', models.CharField(help_text='Введите имя и фамилию докладчика', max_length=100, verbose_name='Имя и фамилия выступающего')),
                ('speciality', models.CharField(help_text='Введите специальность', max_length=1000, verbose_name='Специальность докладчика')),
            ],
            options={
                'verbose_name': 'докладчика',
                'verbose_name_plural': 'Выступающие',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_user_id', models.IntegerField(verbose_name='Телеграм-ID задающего вопрос')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('speaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Conference.speaker', verbose_name='Выступающий')),
            ],
            options={
                'verbose_name': 'вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название выступления')),
                ('description', models.TextField(max_length=5000, verbose_name='Описание выступления')),
                ('time', models.TimeField(help_text='Введите время выступления', verbose_name='Время выступления')),
                ('conference', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='performances', to='Conference.conference', verbose_name='На какой конференции будет выступление')),
                ('speaker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='performances', to='Conference.speaker', verbose_name='Выступающий')),
            ],
            options={
                'verbose_name': 'выступление',
                'verbose_name_plural': 'Выступления',
            },
        ),
    ]
