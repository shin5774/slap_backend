# Generated by Django 3.2.16 on 2023-05-11 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=256)),
                ('is_staff', models.CharField(default='0', max_length=1)),
                ('is_delete', models.CharField(default='0', max_length=1)),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
    ]