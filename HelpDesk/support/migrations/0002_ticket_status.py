# Generated by Django 4.0.2 on 2022-02-15 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('open', 'open'), ('closed', 'closed'), ('at_work', 'at_work')], default='open', max_length=7),
        ),
    ]
